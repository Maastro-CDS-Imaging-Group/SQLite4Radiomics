"""
This module is used as a template for all repositories.
All repositories in the data access layer should inherit from this base class.
"""
import os
from abc import ABC
from typing import Any, Dict, Callable, List, Optional

from dal.database_connector import DatabaseConnector

import pandas as pd


class Repository(ABC):
    """
    This **Abstract Base Class** is used for creating, reading, updating and deleting items in the database.
    """

    def __init__(self, database_connector: DatabaseConnector, queries_file_directory: str) -> None:
        """
        Constructor for class Repository.
        :param database_connector: Instance of class DatabaseConnector which is used to communicate with the database.
        :param queries_file_directory: The directory of the SQL-files.
        """
        self.database_connector: DatabaseConnector = database_connector
        self.query_file_directory: str = queries_file_directory

    @staticmethod
    def read_sql_file(file_path: str) -> str:
        """
        Reads SQL-queries from the SQL-file.
        :param file_path: File path to the SQL File to read.
        :return: The SQL-query in the specified file.
        """

        # Checks if file doesn't exists.
        if not os.path.isfile(file_path):
            # Throws error for not finding SQL-file.
            raise FileNotFoundError("No such file: {0}".format(file_path))

        # Opens SQL-file in read mode.
        with open(file_path) as sql_file:
            # Reads SQL-statement from SQL-file.
            sql_statement: str = sql_file.read()
        # Returns SQL-statement.
        return sql_statement

    def execute_non_query(self, sql_file_path: str, sql_parameters: Dict[str, Any]) -> None:
        """
        Executes SQL-non-query.
        :param sql_file_path: The path of the query used to get the objects from the database.
        :param sql_parameters: The parameters used by the SQL-statement.
        :return: The method doesn't return anything
        """

        # Gets query from SQL-file
        query: str = self.read_sql_file(sql_file_path)

        # Opens a connection with the database.
        with self.database_connector as db_connector:
            # Executes query and stores result in query_result variable.
            db_connector.execute_non_query(query, sql_parameters)
            # Connection with the database will be closed after this point.

    def execute_query(self, sql_file_path: str, sql_parameters: Dict[str, Any]) -> pd.DataFrame:
        """
        Executes SQL-query.
        :param sql_file_path: The path of the query used to get the objects from the database.
        :param sql_parameters: The parameters used by the SQL-statement.
        :return: The returned table from the database.
        """

        # Gets query from SQL-file
        query: str = self.read_sql_file(sql_file_path)

        # Opens a connection with the database.
        with self.database_connector as db_connector:
            # Executes query and stores result in query_result variable.
            return db_connector.execute_query(query, sql_parameters)
            # Connection with the database will be closed after this point.

    def save_object(self, sql_file_path: str, sql_parameters: Dict[str, Any],
                    object_exist_checker: Callable[[Any], bool], *objects_to_save: Any) -> None:
        """
        Saves object to the database.
        :param sql_file_path: The path of the query used to get the objects from the database.
        :param sql_parameters: The parameters used by the SQL-statement.
        :param object_exist_checker: Method that checks whether object already exists.
        :param object_to_save: The object to save.
        :return: The method doesn't return anything
        """

        if object_exist_checker(*objects_to_save):
            return

        self.execute_non_query(sql_file_path, sql_parameters)

    def get_all_by_constrained(self, sql_file_path: str, sql_parameters: Dict[str, Any],
                                           record_to_object_converter: Callable[[pd.Series], Any]):
        """
        Gets all objects matching a criteria.
        :param sql_file_path: The path of the query used to get the objects from the database.
        :param sql_parameters: The parameters used by the SQL-statement.
        :param record_to_object_converter: A method that converts the table row to it's correct object type.
        :return: The objects loaded from the database.
        """

        # Executes the SQL-query in with the given parameters.
        query_result: pd.DataFrame = self.execute_query(sql_file_path, sql_parameters)

        # Creates an empty list to store objects in.
        results: List[Any] = []

        index: int
        record: pd.Series
        # Loops through all records returned by the database.
        for index, record in query_result.iterrows():
            # Converts one row of the returned table into an object and adds this object to the results list.
            results.append(record_to_object_converter(record))
        # Returns the list of objects.
        return results

    def get_single_object_by_constrained(self, sql_file_path: str, sql_parameters: Dict[str, Any],
                                         record_to_object_converter: Callable[[pd.Series], Any],
                                         last_result: bool = False):
        """
        Gets the object corresponding to it's properties.
        :param sql_file_path: The path of the query used to get the object from the database.
        :param sql_parameters: The parameters used by the SQL-statement.
        :param record_to_object_converter: A method that converts the table row to it's correct object type.
        :param last_result: Boolean that makes the program switch between picking the first or last result returned.
        :return: The object loaded from the database.
        """

        # Executes the SQL-query in with the given parameters.
        query_result: pd.DataFrame = self.execute_query(sql_file_path, sql_parameters)

        # Checks whether the database returned no results.
        if query_result.empty:
            # Returns None since no matches were found.
            return None

        # Checks whether it should take the first or the last returned record.
        if last_result:
            # Takes the last result returned by the database.
            record: pd.Series = query_result.tail(1).iloc[0]
        else:
            # Takes the first result returned by the database.
            record: pd.Series = query_result.iloc[0]

        # Converts the row of the returned table to an object and returns this object.
        return record_to_object_converter(record)

    def check_if_object_exist_in_database(self, sql_file_path: str, sql_parameters: Dict[str, Any]):
        """
        Checks whether object is already in the database or not.
        :param sql_file_path: The path to the query used to get the object from the database.
        :param sql_parameters: The parameters used to by the SQL-statement.
        :return: Returns True if object is already in the database and false if it isn't in the database.
        """

        # Executes the SQL-query in with the given parameters.
        query_result: pd.DataFrame = self.execute_query(sql_file_path, sql_parameters)

        # Returns if object already exists in the database.
        return not query_result.empty
