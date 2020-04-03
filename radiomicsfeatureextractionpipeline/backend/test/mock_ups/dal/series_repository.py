from typing import List, Any, Dict, Optional

from dal.database_connector import DatabaseConnector
from dal.series_repository import SeriesRepository
from logic.entities.patient import Patient
from logic.entities.series import Series
from logic.entities.study import Study
from test.mock_ups.dal.repository import RepositoryMockUp


class SeriesRepositoryMockUp(SeriesRepository, RepositoryMockUp):

    def __init__(self, database_connector: DatabaseConnector, query_directory: str) -> None:
        super().__init__(database_connector, query_directory)

        self.get_all_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_series_return_value: Any = None

        self.get_all_series_of_modality_type_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_series_of_modality_type_return_value: Any = None

        self.get_all_series_from_study_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_series_from_study_return_value: Any = None

        self.get_all_series_from_study_of_modality_type_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_series_from_study_of_modality_type_return_value: Any = None

        self.get_all_series_from_patient_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_series_from_patient_return_type: Any = None

        self.get_all_series_from_patient_of_modality_type_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_series_from_patient_of_modality_type_return_type: Any = None

        self.get_series_from_id_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_series_from_id_return_value: Any = None

    def get_all_series(self) -> List[Series]:
        self.get_all_series_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_all_series_return_value

    def get_all_series_of_modality_type(self, modality: str) -> List[Series]:
        self.get_all_series_of_modality_type_called_with_parameters.append(
            {
                'modality': modality
            }
        )
        return self.get_all_series_of_modality_type_return_value

    def get_all_series_from_study(self, study: Study) -> List[Series]:
        self.get_all_series_from_study_called_with_parameters.append(
            {
                'study': study
            }
        )
        return self.get_all_series_from_study_return_value

    def get_all_series_from_study_of_modality_type(self, study: Study, modality: str) -> List[Series]:
        self.get_all_series_from_study_of_modality_type_called_with_parameters.append(
            {
                'study': study,
                'modality': modality
            }
        )
        return self.get_all_series_from_study_of_modality_type_return_value

    def get_all_series_from_patient(self, patient: Patient) -> List[Series]:
        self.get_all_series_from_patient_called_with_parameters.append(
            {
                'patient': patient
            }
        )
        return self.get_all_series_from_patient_return_type

    def get_all_series_from_patient_of_modality_type(self, patient: Patient, modality: str) -> List[Series]:
        self.get_all_series_from_patient_of_modality_type_called_with_parameters.append(
            {
                'patient': patient,
                'modality': modality
            }
        )
        return self.get_all_series_from_patient_of_modality_type_return_type

    def get_series_from_id(self, series_id: str) -> Optional[Series]:
        self.get_series_from_id_called_with_parameters.append(
            {
                'series_id': series_id
            }
        )
        return self.get_series_from_id_return_value

    def get_get_all_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_series_called_with_parameters

    def set_get_all_series_return_value(self, return_value: Any) -> None:
        self.get_all_series_return_value = return_value

    def get_get_all_series_of_modality_type_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_series_of_modality_type_called_with_parameters

    def set_get_all_series_of_modality_type_return_type(self, return_value: Any) -> None:
        self.get_all_series_of_modality_type_return_value = return_value

    def get_get_all_series_from_study_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_series_from_study_called_with_parameters

    def set_get_all_series_from_study_return_value(self, return_value: Any) -> None:
        self.get_all_series_from_study_return_value = return_value

    def get_get_all_series_from_study_of_modality_type_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_series_from_study_of_modality_type_called_with_parameters

    def set_get_all_series_from_study_of_modality_type_return_value(self, return_value: Any):
        self.get_all_series_from_study_of_modality_type_return_value = return_value

    def get_get_all_series_from_patient_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_series_from_patient_called_with_parameters

    def set_get_all_series_from_patient_return_value(self, return_value = Any) -> None:
        self.get_all_series_from_patient_return_type = return_value

    def get_get_all_series_from_patient_of_modality_type_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_series_from_patient_of_modality_type_called_with_parameters

    def set_get_all_series_from_patient_of_modality_type_return_value(self, return_value: Any) -> None:
        self.get_all_series_from_patient_of_modality_type_return_type = return_value

    def get_get_series_from_id_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_series_from_id_called_with_parameters

    def set_get_series_from_id_return_value(self, return_value: Optional[Series]):
        self.get_series_from_id_return_value = return_value
