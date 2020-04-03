from typing import List, Optional, Any, Dict

from dal.database_connector import DatabaseConnector
from dal.patient_repository import PatientRepository
from logic.entities.patient import Patient
from test.mock_ups.dal.repository import RepositoryMockUp


class PatientRepositoryMockUp(PatientRepository, RepositoryMockUp):

    def __init__(self, database_connector: DatabaseConnector, query_directory: str) -> None:
        super().__init__(database_connector, query_directory)

        self.get_all_patients_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_patients_return_value: Any = None

        self.get_patient_by_id_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_patient_by_id_return_value: Any = None

    def get_all_patients(self) -> List[Patient]:
        self.get_all_patients_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_all_patients_return_value

    def get_patient_by_id(self, patient_id: str) -> Optional[Patient]:
        self.get_patient_by_id_called_with_parameters.append(
            {
                'patient_id': patient_id
            }
        )
        return self.get_patient_by_id_return_value

    def get_get_all_patients_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_patients_called_with_parameters

    def set_get_all_patients_return_value(self, return_value: Any) -> None:
        self.get_all_patients_return_value = return_value

    def get_get_patient_by_id_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_patient_by_id_called_with_parameters

    def set_get_patient_by_id_return_value(self, return_value: Any) -> None:
        self.get_patient_by_id_return_value = return_value
