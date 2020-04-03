from typing import List, Dict, Any, Optional

from dal.database_connector import DatabaseConnector
from dal.repository import Repository


class RepositoryMockUp(Repository):

    read_sql_file_called_with_parameters: List[Dict[Optional[str], Any]] = []
    read_sql_file_return_value: Any = None

    def __init__(self, database_connector: DatabaseConnector, queries_file_directory: str) -> None:
        super().__init__(database_connector, queries_file_directory)

    @staticmethod
    def read_sql_file(file_path: str) -> str:
        RepositoryMockUp.read_sql_file_called_with_parameters.append(
            {
                'file_path': file_path
            }
        )
        return RepositoryMockUp.read_sql_file_return_value

    def get_read_sql_file_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return RepositoryMockUp.read_sql_file_called_with_parameters

    def set_get_sql_file_return_value(self, return_value: Any) -> None:
        RepositoryMockUp.read_sql_file_return_value = return_value