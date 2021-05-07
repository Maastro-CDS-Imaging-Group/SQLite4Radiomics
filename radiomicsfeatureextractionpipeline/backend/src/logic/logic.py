"""
This module serves as a facade class for the core functionality of the tool.
"""

import datetime
import logging
from typing import List, Tuple, Dict
import tempfile
import shutil

import SimpleITK as sitk

from configuration_service.configuration_service import ConfigurationService
from dal.data_access_layer import DataAccessLayer
from logic.binary_mask_and_3d_image_generator.binary_mask_and_3d_image_generator import \
    BinaryMaskAnd3DImageGenerator
from logic.dicom_file_reader.dicom_file_reader import DicomFileReader
from logic.feature_extractor.feature_calculator import FeatureCalculator
from logic.entities.image import Image
from logic.entities.patient import Patient
from logic.entities.radiomic_calculation import RadiomicCalculation
from logic.entities.roi import ROI
from logic.roi_selector.roi_selector import ROISelector
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series import Series
from logic.entities.series_with_image_slices import SeriesWithImageSlices
from logic.dicom_file_reader.image_reader import read_dcm_series, write_with_sitk

from pathlib import Path

import subprocess
import time

from logic.utils.logging_utils import setup_logging


logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
setup_logging(filename='logs/logic.log', name=__name__)


perf_logger: logging.Logger = logging.getLogger('performance')
perf_logger.setLevel(logging.DEBUG)



class Logic:
    """
    This class functions as the facade class of the core logic of the tool. It provides methods that can be called by
    user interface and by commandline.
    """

    def __init__(self, data_access_layer: DataAccessLayer, conquest_settings: ConfigurationService,
                 feature_extraction_settings: ConfigurationService, roi_selector: ROISelector = None,
                 binary_mask_and_3d_image_generator: BinaryMaskAnd3DImageGenerator = None,
                 dicom_file_reader: DicomFileReader = None,
                 radiomic_feature_calculator: FeatureCalculator = None) -> None:
        """
        The constructor of the Logic class.
        :param data_access_layer: The data_access_layer that will be used to access the data in the database.
        :param conquest_settings: The configuration manager that reads the properties of conquest.
        :param feature_extraction_settings: The configuration manager that reads the properties of the radiomic tool.
        :param roi_selector: The roi selector that will select the ROI's that will be used for calculating the radiomic
        features.
        :param binary_mask_and_3d_image_generator: The binary mask and 3d image generator that is used for generating
        the 3d image from the series with image slicing and the binary mask from the RTSTRUCT-series.
        :param dicom_file_reader: The DICOM-file reader that will be used for reading the DICOM-files.
        :param radiomic_feature_calculator: The radiomic feature calculator that is used for calculating the radiomic
        features.
        """

        # All the fields for storing all the instances that the logic class uses.
        self.data_access_layer: DataAccessLayer = data_access_layer
        self.feature_extraction_settings: ConfigurationService = feature_extraction_settings
        self.conquest_settings: ConfigurationService = conquest_settings
        self.dicom_file_reader: DicomFileReader = dicom_file_reader
        self.binary_mask_generator: BinaryMaskAnd3DImageGenerator = binary_mask_and_3d_image_generator
        self.parameter_file: str = self.feature_extraction_settings.load_radiomics_params_file()
        self.radiomic_feature_calculator: FeatureCalculator = radiomic_feature_calculator
        self.roi_selector: ROISelector = roi_selector
        self.data_path: Path = Path('../conquest/data').resolve()
        self.plastimatch_path: Path = Path("tools/Plastimatch/bin/plastimatch.exe").resolve()

    def get_patient_overview(self) -> List[Patient]:
        """
        Gets a list of all the patients in the database.
        :return: A list of all patients in the database.
        """
        return self.data_access_layer.get_patient_repos().get_all_patients()

    def get_overview_of_patients_series(self, patient: Patient) -> List[Series]:
        """
        Gets a list of all series stored in the database that belong to the given patient.
        :param patient: The patient to filter the series with.
        :return: A filtered list of series stored in the database.
        """
        return self.data_access_layer.get_series_repos().get_all_series_from_patient(patient)

    def get_rois_with_undefined_priorities(self) -> List[ROI]:
        """
        Gets a list of all rois with an undefined priority.
        :return: A list of all ROI's that have no set priority.
        """
        return self.data_access_layer.get_roi_repos().get_rois_of_priority(-1)

    def update_roi_priority(self, roi: ROI) -> None:
        """
        Updates the priority value for the given ROI.
        :param roi: The ROI with the changed priority.
        :return: The method doesn't return anything.
        """
        self.data_access_layer.get_roi_repos().update_roi_priority(roi)

    def extract_features(self, sop_instance_rtstruct: str) -> None:
        """
        Extracts the radiomic features for the studies that have a rtstruct file with a SOP-Instance that corresponds
        to the provided SOP-instance
        :param sop_instance_rtstruct: The SOP-instance of the RTSTRUCT that will be used for calculating the radiomic
        features.
        :return: The method doesn't return anything.
        """

        # Loads the patient data, the RTSTRUCT-series data and the CT-, PET- or MRI-series that are connected to the
        # SOP-instance.
        patient_series_instances: List[Tuple[Patient, RtstructSeries, SeriesWithImageSlices]] = \
            self.data_access_layer.get_image_repos().get_images_of_patients_last_ct_series_matching_rtstruct(
                sop_instance_rtstruct)

        # Loops though all the matches found.
        for patient_series_instance in patient_series_instances:

            # Extracts the patient out of the found result.
            patient: Patient = patient_series_instance[0]
            # Extracts the RTSTRUCT-series out of the found result.
            rtstruct_series: RtstructSeries = patient_series_instance[1]
            # Extracts the CT-, PET- or MRI-Series out of the found result.
            series_of_image_slices: SeriesWithImageSlices = patient_series_instance[2]

            # Loads the path of the DICOM-file from the CT-, PET- or MRI- series' images.
            dicom_paths: List[Path] = [self.data_path / image.object_file for image in series_of_image_slices.images]
    
            subject_folder = tempfile.TemporaryDirectory()

            # Copy dicom paths of a particular series into subject folder
            for dicom_path in dicom_paths:
                dicom_path = dicom_path.resolve()
                shutil.copy(dicom_path, Path(subject_folder.name) / dicom_path.name)


            # Loads the sitk_image and data from the DICOM paths!
            data, image, metadata = read_dcm_series(dicom_paths, return_sitk=True)


            # Loads the data of the DICOM-file from the RTSTRUCT-series image.
            rtstruct: Image = self.dicom_file_reader.read_dicom_file(rtstruct_series.image)

            # Checks whether the rtstruct DICOM-files were property loaded.
            if rtstruct is None:
                # When there was an error loading the DICOM-file of the RTSTRUCT the program will skip the calculation
                # of the radiomic features.
                continue

            rtstruct_filename: Path = (self.data_path / rtstruct.object_file).resolve()


            # Create intermediate directory for plastimatch artifacts
            intermediate_dir = tempfile.TemporaryDirectory()

            intermediate_path: Path = Path(intermediate_dir.name)


            image_path = intermediate_path.resolve() / "image.nrrd"

            write_with_sitk(image, image_path)



            plastimatch_start_time: float = time.perf_counter()

            plastimatch_command = f"{str(self.plastimatch_path)} convert --input {str(rtstruct_filename)} --referenced-ct {str(subject_folder.name)} \
--output-prefix {str(intermediate_path)} --prefix-format nrrd --fixed {str(image_path)}"

            logger.info(f"Running plastimatch command: {plastimatch_command}")
            out = subprocess.check_output(plastimatch_command.split())

            plastimatch_run_time: float = time.perf_counter() - plastimatch_start_time

            perf_logger.info(f"Took {plastimatch_run_time} to run plastimatch conversion")

            # Loads all the ROI's from the RTSTRUCT.
            rois: Dict[ROI, int] = self.roi_selector.get_rois_of_rtstruct(rtstruct)
            # Saves all the ROI's found in the RTSTRUCT. ROI already in the database will be ignored!
            self.roi_selector.save_rois_from_rtstruct(rois, rtstruct_series)
            # Loads all the ROI's. The ROI's will now have their identity set.
            rois: List[ROI] = self.roi_selector.select_rois(rtstruct_series)

            # Checks if there are ROI's found or not.
            if len(rois) == 0:
                # When no ROI's were found the program will skip the calculation of the radiomic features.
                continue

            # Stores all basic information about the radiomic calculation to the database.
            radiomic_calculation: RadiomicCalculation = RadiomicCalculation(
                patient, rtstruct_series, series_of_image_slices, datetime.datetime.now())
            self.data_access_layer.get_radiomic_feature_repos().save_radiomic_calculation(radiomic_calculation)
            radiomic_calculation: RadiomicCalculation = self.data_access_layer.get_radiomic_feature_repos()\
                .get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices(patient, rtstruct_series,
                                                                                           series_of_image_slices)

            logger.info("Calculating the features for {} ROI's".format(len(rois)))
            succesful_feature_calculations: int = 0

            roi: ROI

            # Calculates radiomic feature for all ROI's.
            pyradiomics_start_time: float = time.perf_counter()

            for roi in rois:

                roi_start_time: float = time.perf_counter()

                # Gets the number of the roi from the database.
                roi_number: int = self.data_access_layer.roi_repos.get_dicom_segmentation(rtstruct_series, roi).number

                logger.info("Generating feature for roi {0}".format(roi.name))

                # Tries to generate a 3d image and a binary mask from the given rtstruct, image_slices and roi.
                try:
                    mask_path = (intermediate_path / (roi.name + ".nrrd")).resolve()
                    mask = sitk.ReadImage(str(mask_path))                                                               

                except (IndexError, AttributeError, TypeError):
                    # Failed to generate the binary mask and 3d image. The calculation for the ROI will be skipped.
                    logger.error("An exception occurred while generation binary mask and 3d image for roi {0}".format(
                        roi.name))
                    logger.error("Skipping feature extraction for roi {0}".format(roi.name))
                    continue

                # Tries to calculate the radiomic features for the given 3d image, binary mask and roi.
                try:
                    result = self.radiomic_feature_calculator.calculate_features(radiomic_calculation, image,  mask, roi, return_result=True)
                except (RuntimeError, ValueError):
                    # Failed to calculate the radiomic features. The calculation for the ROI will be skipped.
                    logger.error("An exception occurred while calculating the features for roi {0}".format(roi.name))
                    logger.error("Skipping feature extraction for roi {0}".format(roi.name))
                    continue

                # Successfully calculated the radiomic features for the ROI. Logging the performance.
                roi_run_time: float = time.perf_counter() - roi_start_time
                perf_logger.info(f"Took {roi_run_time} to run the calculation for {roi.name} ROI.")
                perf_logger.info(f"Took {roi_run_time / result['original_shape_VoxelVolume']} normalized by VoxelVolume to run the calculation for {roi.name} ROI with {result['original_shape_VoxelVolume']} volume")
                perf_logger.info(f"Took {roi_run_time / result['diagnostics_Mask-original_VoxelNum']} normalized by VoxelNum to run the calculation for {roi.name} ROI with {result['diagnostics_Mask-original_VoxelNum']} voxels")
                
                logger.info("Successfully extracted features for roi {0}".format(roi.name))
                succesful_feature_calculations += 1

            logger.info("Successfully calculated radiomic features for {0} of {1} ROI's".format(
                succesful_feature_calculations, len(rois)))


            pyradiomics_run_time: float = time.perf_counter() - pyradiomics_start_time

            perf_logger.info(f"Took {pyradiomics_run_time} to run pyradiomics feature extraction over all selected ROIs")
            


            # Gets a path to the csv file with all calculated results.
            self.data_access_layer.get_radiomic_feature_repos().get_radiomic_calculation_result(
                radiomic_calculation.identity)


            intermediate_dir.cleanup()
