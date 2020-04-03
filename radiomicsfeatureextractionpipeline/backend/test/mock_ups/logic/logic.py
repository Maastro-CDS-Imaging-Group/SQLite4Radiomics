from typing import List, Optional, Dict, Any

from configuration_service.configuration_service import ConfigurationService
from dal.data_access_layer import DataAccessLayer
from logic.binary_mask_and_3d_image_generator.binary_mask_and_3d_image_generator import BinaryMaskAnd3DImageGenerator
from logic.dicom_file_reader.dicom_file_reader import DicomFileReader
from logic.feature_extractor.feature_calculator import FeatureCalculator
from logic.logic import Logic
from logic.entities.patient import Patient
from logic.entities.roi import ROI
from logic.roi_selector.roi_selector import ROISelector
from logic.entities.series import Series


class LogicMockUp(Logic):

    def __init__(self, data_access_layer: DataAccessLayer, conquest_settings: ConfigurationService,
                 feature_extraction_settings: ConfigurationService, roi_selector: ROISelector = None,
                 binary_mask_and_3d_image_generator: BinaryMaskAnd3DImageGenerator = None,
                 dicom_file_reader: DicomFileReader = None,
                 radiomic_feature_calculator: FeatureCalculator = None) -> None:

        super().__init__(data_access_layer, conquest_settings, feature_extraction_settings, roi_selector,
                         binary_mask_and_3d_image_generator, dicom_file_reader, radiomic_feature_calculator)

        self.get_patient_overview_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_patient_overview_return_value: Any = None

        self.get_overview_of_patients_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_overview_of_patients_series_return_value: Any = None

        self.get_rois_with_undefined_priorities_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_rois_with_undefined_priorities_return_value: Any = None

        self.update_roi_priority_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.update_roi_priority_return_value: Any = None

        self.extract_features_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.extract_features_return_value: Any = None

    def get_patient_overview(self) -> List[Patient]:
        self.get_patient_overview_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_patient_overview_return_value

    def get_overview_of_patients_series(self, patient: Patient) -> List[Series]:
        self.get_overview_of_patients_series_called_with_parameters.append(
            {
                'patient': patient
            }
        )
        return self.get_overview_of_patients_series_return_value

    def get_rois_with_undefined_priorities(self) -> List[ROI]:
        self.get_rois_with_undefined_priorities_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_rois_with_undefined_priorities_return_value

    def update_roi_priority(self, roi: ROI) -> None:
        self.update_roi_priority_called_with_parameters.append(
            {
                'roi': roi
            }
        )
        return self.update_roi_priority_return_value

    def extract_features(self, sop_instance_rtstruct: str) -> None:
        self.extract_features_called_with_parameters.append(
            {
                'sop_instance_rtstruct': sop_instance_rtstruct
            }
        )

    def get_get_patient_overview_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_patient_overview_called_with_parameters

    def set_get_patient_overview_return_value(self, return_value: Any) -> None:
        self.get_patient_overview_return_value = return_value

    def get_get_overview_of_patients_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_overview_of_patients_series_called_with_parameters

    def set_get_overview_of_patients_series_return_value(self, return_value: Any) -> None:
        self.get_overview_of_patients_series_return_value = return_value

    def get_get_rois_with_undefined_priorities_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_rois_with_undefined_priorities_called_with_parameters

    def set_get_rois_with_undefined_priorities_return_value(self, return_value: Any) -> None:
        self.get_rois_with_undefined_priorities_return_value = return_value

    def get_update_roi_priority_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.update_roi_priority_called_with_parameters

    def set_update_roi_priority_return_value(self, return_value: Any) -> None:
        self.update_roi_priority_return_value = return_value

    def get_extract_features_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.extract_features_called_with_parameters

    def set_extract_features_return_value(self, return_value: Any) -> None:
        self.extract_features_return_value = return_value
