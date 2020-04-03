from typing import List, Optional, Dict, Any

from dal.sqlite.database_connector_sqlite import DatabaseConnectorSqlite
from dal.study_repository import StudyRepository
from logic.entities.study import Study
from test.mock_ups.dal.repository import RepositoryMockUp


class StudyRepositoryMockUp(StudyRepository, RepositoryMockUp):

    def __init__(self, database_connector: DatabaseConnectorSqlite, query_directory: str) -> None:
        super().__init__(database_connector, query_directory)

        self.get_all_studies_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_studies_return_value: Any = None

        self.get_study_by_id_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_study_by_id_return_value: Any = None

    def get_all_studies(self) -> List[Study]:
        self.get_all_studies_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_all_studies_return_value

    def get_study_by_id(self, study_id: str) -> Optional[Study]:
        self.get_study_by_id_called_with_parameters.append(
            {
                'study_id': study_id
            }
        )
        return self.get_study_by_id_return_value

    def get_get_all_studies_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_studies_called_with_parameters

    def set_get_all_studies_return_value(self, return_value: Any) -> None:
        self.get_all_studies_return_value = return_value

    def get_get_study_by_id_called_with_parameters(self) -> List:
        return self.get_study_by_id_called_with_parameters

    def set_get_study_by_id_return_value(self, return_value: Any) -> None:
        self.get_study_by_id_return_value = return_value
