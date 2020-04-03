"""
This module is used as a template for all database connectors.
All database connectors should inherit from this base class.
"""

import os
from abc import ABC, abstractmethod
from typing import Any, Optional

import pandas as pd


class DatabaseConnector(ABC):
    """
    This **Abstract Base Class** is used for:
    - Establishing a connection with the database.
    - Querying the data of the database.
    - Insert, update, delete data of the database.
    """

    def __init__(self, connection_string: str) -> None:
        """
        Constructor for DatabaseConnector class
        :param connection_string: contains the connection string that is used for connecting with the database
        """
        self.connection_string: Optional[str] = None
        self.set_connection_string(connection_string)
        self.conn: Optional[DatabaseConnector] = None

    def __enter__(self) -> 'DatabaseConnector':
        """
        Opens connection with database when called by context manager
        :return: returns database connector object to connect with the Database.
        """
        self.open_connection()
        return self

    def __exit__(self, exception_type: Any, exception_value: Any, traceback: Any) -> None:
        """
        Closes the connection with the database. Automatically called at the end of context manager
        :param exception_type: The type of exception that occurred while connection was open.
        :param exception_value: The value of the exception that occurred while connection was open.
        :param traceback: The traceback of the exception that occurred while connection was open.
        """
        self.close_connection()

    def set_connection_string(self, connection_string: str) -> None:
        """
        Changes the connection string so it will connect to a different database
        :param connection_string: The new connection string that will override the existing one.
        """
        self.connection_string: str = connection_string

    @abstractmethod
    def open_connection(self) -> None:
        """
        Opens the connection with the database
        """
        pass

    @abstractmethod
    def execute_non_query(self, sql_query: str, arg: Optional[Any]) -> None:
        """
        Executes all queries that don't return values:
        - CREATE
        - DROP
        - INSERT
        - UPDATE
        - DELETE
        :param sql_query: The query to be executed.
        :param arg: The arguments to pass into the query.
        """
        pass

    @abstractmethod
    def execute_query(self, sql_query: str, arg: Optional[Any]) -> pd.DataFrame:
        """
        Executes SELECT statements and returns result in a pandas.DataFrame.
        :param sql_query: The query to be executed.
        :param arg: The arguments to pass into the query
        :return: pandas.DataFrame with query result
        """
        pass

    @abstractmethod
    def close_connection(self) -> None:
        """
        Closes the connection with the database
        """
        pass
