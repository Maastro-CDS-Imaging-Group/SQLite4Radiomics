from typing import Any, Optional, Dict, List

import pandas as pd

from dal.database_connector import DatabaseConnector


class DatabaseConnectorMockUp(DatabaseConnector):

    def __init__(self, connection_sting: str) -> None:
        super().__init__(connection_sting)

        self.open_connection_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.open_connection_return_value: Any = None

        self.execute_non_query_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.execute_non_query_return_value: Any = None

        self.execute_query_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.execute_query_result_value: Any = None

        self.close_connection_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.close_connection_return_value = None

    def open_connection(self) -> None:
        self.open_connection_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.open_connection_return_value

    def execute_non_query(self, sql_query: str, arg: Optional[Any]) -> None:
        self.execute_non_query_called_with_parameters.append(
            {
                'sql_query': sql_query,
                'arg': arg
            }
        )
        return self.execute_non_query_return_value

    def execute_query(self, sql_query: str, arg: Optional[Any]) -> pd.DataFrame:
        self.execute_query_called_with_parameters.append(
            {
                'sql_query': sql_query,
                'arg': arg
            }
        )
        return self.execute_query_result_value

    def close_connection(self) -> None:
        self.close_connection_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.close_connection_return_value

    def get_open_connection_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.open_connection_called_with_parameters

    def set_open_connection_return_value(self, return_value: Any) -> None:
        self.open_connection_return_value = return_value

    def get_execute_non_query_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.execute_non_query_called_with_parameters

    def set_execute_non_query_return_value(self, return_value: Any):
        self.execute_non_query_return_value = return_value

    def get_execute_query_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.execute_query_called_with_parameters

    def set_execute_query_result_value(self, result_value: Any) -> None:
        self.execute_query_result_value: pd.DataFrame = result_value

    def get_close_connection_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.close_connection_called_with_parameters

    def set_close_connection_return_value(self, return_value: str) -> None:
        self.close_connection_return_value = return_value
