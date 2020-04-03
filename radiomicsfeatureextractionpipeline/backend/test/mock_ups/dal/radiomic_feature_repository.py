from typing import Optional, Dict, Any, List

from dal.database_connector import DatabaseConnector
from dal.patient_repository import PatientRepository
from dal.radiomic_feature_repository import RadiomicFeatureRepository
from dal.series_repository import SeriesRepository
from logic.entities.patient import Patient
from logic.entities.radiomic_calculation import RadiomicCalculation
from logic.entities.radiomic_class import RadiomicClass
from logic.entities.radiomic_feature import RadiomicFeature
from logic.entities.radiomic_feature_value import RadiomicFeatureValue
from logic.entities.radiomic_filter import RadiomicFilter
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series_with_image_slices import SeriesWithImageSlices
from test.mock_ups.dal.repository import RepositoryMockUp


class RadiomicFeatureRepositoryMockUp(RadiomicFeatureRepository, RepositoryMockUp):

    def __init__(self, database_connector: DatabaseConnector, patient_repos: PatientRepository,
                 series_repository: SeriesRepository, query_directory: str) -> None:
        super().__init__(database_connector, patient_repos, series_repository, query_directory)

        self.save_radiomic_feature_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_radiomic_feature_return_value: Any = None

        self.save_radiomic_filter_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_radiomic_filter_return_value: Any = None

        self.save_radiomic_class_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_radiomic_class_return_value: Any = None

        self.save_radiomic_feature_value_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_radiomic_feature_value_return_value: Any = None

        self.save_radiomic_calculation_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_radiomic_calculation_return_value: Any = None

        self.radiomic_feature_exists_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.radiomic_feature_exists_return_value: Any = None

        self.radiomic_filter_exists_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.radiomic_filter_exists_return_value: Any = None

        self.radiomic_class_exists_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.radiomic_class_exists_return_value: Any = None

        self.get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices_called_with_parameters: List[
            Dict[Optional[str], Any]] = []
        self.get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices_return_value: Any = None

        self.get_radiomic_filter_by_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_filter_by_name_return_value: Any = None

        self.get_radiomic_feature_by_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_feature_by_name_return_value: Any = None

        self.get_radiomic_class_by_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_class_by_name_return_value: Any = None

        self.get_radiomic_class_by_id_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_class_by_id_return_value: Any = None

        self.get_radiomic_calculation_result_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_calculation_result_return_value: Any = None

    def save_radiomic_feature(self, radiomic_feature: RadiomicFeature) -> None:
        self.save_radiomic_feature_called_with_parameters.append(
            {
                'radiomic_feature': radiomic_feature
            }
        )
        return self.save_radiomic_feature_return_value

    def save_radiomic_filter(self, radiomic_filter: RadiomicFilter) -> None:
        self.save_radiomic_filter_called_with_parameters.append(
            {
                'radiomic_filter': radiomic_filter
            }
        )
        return self.save_radiomic_filter_return_value

    def save_radiomic_class(self, radiomic_class: RadiomicClass):
        self.save_radiomic_class_called_with_parameters.append(
            {
                'radiomic_class': radiomic_class
            }
        )
        return self.save_radiomic_class_return_value

    def save_radiomic_feature_value(self, radiomic_calculation: RadiomicCalculation,
                                    radiomic_feature_value: RadiomicFeatureValue):
        self.save_radiomic_feature_value_called_with_parameters.append(
            {
                'radiomic_calculation': radiomic_calculation,
                'radiomic_feature_value': radiomic_feature_value
            }
        )
        return self.save_radiomic_feature_value_return_value

    def save_radiomic_calculation(self, radiomic_calculation: RadiomicCalculation):
        self.save_radiomic_calculation_called_with_parameters.append(
            {
                'radiomic_calculation': radiomic_calculation
            }
        )
        return self.save_radiomic_calculation_return_value

    def radiomic_feature_exists(self, radiomic_feature: RadiomicFeature) -> bool:
        self.radiomic_feature_exists_called_with_parameters.append(
            {
                'radiomic_feature': radiomic_feature
            }
        )
        return self.radiomic_feature_exists_return_value

    def radiomic_filter_exists(self, radiomic_filter: RadiomicFilter) -> bool:
        self.radiomic_filter_exists_called_with_parameters.append(
            {
                'radiomic_filter': radiomic_filter
            }
        )
        return self.radiomic_filter_exists_return_value

    def radiomic_class_exists(self, radiomic_class: RadiomicClass) -> bool:
        self.radiomic_filter_exists_called_with_parameters.append(
            {
                'radiomic_class': radiomic_class
            }
        )
        return self.radiomic_class_exists_return_value

    def get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices(
            self, patient: Patient, rtstruct_series: RtstructSeries,
            ct_series: SeriesWithImageSlices) -> RadiomicCalculation:
        self.get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices_called_with_parameters.append(
            {
                'patient': Patient,
                'rtstruct_series': RtstructSeries,
                'ct_series': SeriesWithImageSlices
            }
        )
        return self.get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices_return_value

    def get_radiomic_filter_by_name(self, name: str) -> RadiomicFilter:
        self.get_radiomic_filter_by_name_called_with_parameters.append(
            {
                'name': name
            }
        )
        return self.get_radiomic_filter_by_name_return_value

    def get_radiomic_feature_by_name(self, name: str) -> RadiomicFeature:
        self.get_radiomic_feature_by_name_called_with_parameters.append(
            {
                'name': name
            }
        )
        return self.get_radiomic_feature_by_name_return_value

    def get_radiomic_class_by_name(self, name: str) -> RadiomicClass:
        self.get_radiomic_class_by_name_called_with_parameters.append(
            {
                'name': name
            }
        )
        return self.get_radiomic_class_by_name_return_value

    def get_radiomic_class_by_id(self, radiomic_class_id: int) -> RadiomicClass:
        self.get_radiomic_class_by_id_called_with_parameters.append(
            {
                'radiomic_class_id': radiomic_class_id
            }
        )
        return self.get_radiomic_class_by_id_return_value

    def get_radiomic_calculation_result(self, radiomic_calculation_id: int) -> RadiomicCalculation:
        self.get_radiomic_calculation_result_called_with_parameters.append(
            {
                'radiomic_calculation_id': radiomic_calculation_id
            }
        )
        return self.get_radiomic_calculation_result_return_value

    def get_save_radiomic_feature_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_radiomic_feature_called_with_parameters

    def set_save_radiomic_feature_return_value(self, return_value: Any) -> None:
        self.save_radiomic_feature_return_value = return_value

    def get_save_radiomic_filter_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_radiomic_filter_called_with_parameters

    def set_save_radiomic_filter_return_value(self, return_value: Any) -> None:
        self.save_radiomic_filter_return_value = return_value

    def get_save_radiomic_class_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_radiomic_class_called_with_parameters

    def set_save_radiomic_class_return_value(self, return_value: Any) -> None:
        self.save_radiomic_class_return_value = return_value

    def get_save_radiomic_feature_value_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_radiomic_feature_value_called_with_parameters

    def set_save_radiomic_feature_value_return_value(self, return_value: Any) -> None:
        self.save_radiomic_feature_value_return_value = return_value

    def get_save_radiomic_calculation_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_radiomic_calculation_called_with_parameters

    def set_save_radiomic_calculation_return_value(self, return_value: Any) -> None:
        self.save_radiomic_calculation_return_value = return_value

    def get_radiomic_feature_exists_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.radiomic_feature_exists_called_with_parameters

    def set_radiomic_feature_exists_return_value(self, return_value: Any) -> None:
        self.radiomic_feature_exists_return_value = return_value

    def get_radiomic_filter_exists_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.radiomic_filter_exists_called_with_parameters

    def set_radiomic_filter_exists_return_value(self, return_value: Any) -> None:
        self.radiomic_feature_exists_return_value = return_value

    def get_radiomic_class_exists_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.radiomic_class_exists_called_with_parameters

    def set_radiomic_class_exists_return_value(self, return_value: Any) -> None:
        self.radiomic_class_exists_return_value = return_value

    def get_get_calculation_by_patient_and_series_with_image_slices_called_with_parameters(self) -> List[
            Dict[Optional[str], Any]]:
        return self.get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices_called_with_parameters

    def set_get_calculation_by_patient_and_series_with_image_slices_return_value(self, return_value: Any) -> None:
        self.get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices_return_value = return_value

    def get_get_filter_by_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_filter_by_name_called_with_parameters

    def set_get_filter_by_name_return_value(self, return_value: Any) -> None:
        self.get_radiomic_filter_by_name_return_value = return_value

    def get_get_radiomic_feature_by_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_feature_by_name_called_with_parameters

    def set_get_radiomic_feature_by_name_return_value(self, return_value: Any) -> None:
        self.get_radiomic_feature_by_name_return_value = return_value

    def get_get_radiomic_class_by_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_class_by_name_called_with_parameters

    def set_get_radiomic_class_by_name_return_value(self, result_value: Any) -> None:
        self.get_radiomic_class_by_name_return_value = result_value

    def get_get_radiomic_class_by_id_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_class_by_id_called_with_parameters

    def set_get_radiomic_class_by_id_return_value(self, return_value: Any) -> None:
        self.get_radiomic_class_by_id_return_value = return_value

    def get_get_radiomic_calculation_result_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_calculation_result_called_with_parameters

    def set_get_radiomic_calculation_result_return_value(self, return_value: Any) -> None:
        self.get_radiomic_calculation_result_return_value = return_value
