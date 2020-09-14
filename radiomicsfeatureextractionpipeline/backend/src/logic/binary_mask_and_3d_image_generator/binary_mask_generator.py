import os
from typing import List, Tuple, Optional, Any

import SimpleITK as sitk
import numpy as np
import pydicom
from skimage import draw
from pathlib import Path

from logic.binary_mask_and_3d_image_generator.binary_mask_and_3d_image_generator import \
    BinaryMaskAnd3DImageGenerator
from logic.dicom_file_reader.image_reader import read_dcm_series, write_with_sitk
from logic.entities.image import Image
from logic.entities.roi import ROI

import subprocess


class BinaryMaskGenerator(BinaryMaskAnd3DImageGenerator):

    def generate_binary_mask_and_3d_image(self, image_slices: List[Image], rtstruct_image: Image, roi: ROI,
                                          roi_number: int):
        return self.image_pre_processing(image_slices, rtstruct_image, roi)

    def image_pre_processing(self, images_slices: List[Image], rtstruct_image: Image, roi: ROI) -> Tuple[sitk.Image,
                                                                                                         sitk.Image]:
        """
        :param images_slices: List of Image type data corresponding to indidivual dicom files
        :param rtstruct_image: Image corresponding to one single rtstruct
        :param roi: ROI type corresponding to a particular ROI
        """
        
        # Initialize path location where the data is stored.
        data_path: Path = Path('../conquest/data').resolve()


        # Load paths to RTSTRUCT and DICOM files
        rtstruct_filename: Path = (data_path / rtstruct_image.object_file).resolve()

        dicom_paths: List[Path] = [data_path / image.object_file for image in images_slices]
        
        subject_folder = dicom_paths[0].parent.resolve()

        # Read DICOM Series
        data, sitk_image, metadata = read_dcm_series(dicom_paths, return_sitk=True)


        intermediate_path: Path = Path("intermediate")
        intermediate_path.mkdir(parents=True, exist_ok=True)

        image_path = intermediate_path.resolve() / "image.nrrd"

        write_with_sitk(sitk_image, image_path)

        plastimatch_path: Path = Path("tools/bin/plastimatch.exe").resolve()

        if rtstruct_filename:
            # Plastimatch for generating nrrd for rtstructs!
            plastimatch_command = f"{str(plastimatch_path)} convert --input {str(rtstruct_filename)} --referenced-ct {str(subject_folder)} \
                    --output-prefix {str(intermediate_path)} --prefix-format nrrd --fixed {str(image_path)}"

            print(plastimatch_command.split())
            out = subprocess.check_output(plastimatch_command.split())
        
        mask_path = (intermediate_path / (roi.name + ".nrrd")).resolve()

        mask = sitk.ReadImage(str(mask_path))

        return sitk_image, mask
