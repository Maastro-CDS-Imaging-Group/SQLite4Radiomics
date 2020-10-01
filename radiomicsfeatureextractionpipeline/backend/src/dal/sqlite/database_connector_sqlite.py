"""
This module is used as a template for all database connectors.
"""
import errno
import logging
import os
import sqlite3
from typing import Any, Optional

import pandas as pd

from dal.database_connector import DatabaseConnector
from logic.utils.logging_utils import setup_logging


logger: logging.Logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

error_logger_formatter: logging.Formatter = logging.Formatter('%(asctime)s:%(name):%(message)s')

logger_path: str = 'logs/database_connector.log'

if not os.path.exists(logger_path):
    if not os.path.exists(os.path.dirname(logger_path)):
        try:
            os.makedirs(os.path.dirname(logger_path))
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
    open(logger_path, 'w+')



setup_logging(filename=logger_path, name=__name__)


class DatabaseConnectorSqlite(DatabaseConnector):
    """
    This **Abstract Base Class** is used for:
    - Establishing a connection with the database.
    - Querying the data of the database.
    - Insert, update, delete data of the database.
    """

    conn: Optional[sqlite3.Connection]
    connection_string: str

    def __init__(self, connection_string: str) -> None:
        """
        Constructor for DatabaseConnector class
        :param connection_string: contains the connection string that is used for connecting with the database
        """
        super().__init__(connection_string)

    def open_connection(self) -> None:
        """
        Opens the connection with the database
        """
        logger.debug("Connection Open")
        logger.debug(self.connection_string)
        self.conn: sqlite3.Connection = sqlite3.connect(self.connection_string)
        
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
        cursor: sqlite3.Cursor = self.conn.cursor()
        if arg:
            cursor.execute(sql_query, arg)
        else:
            cursor.execute(sql_query)
        self.conn.commit()
    
    def execute_query(self, sql_query: str, arg: Optional[Any]) -> pd.DataFrame:
        """
        Executes SELECT statements and returns result in a pandas.DataFrame.
        :param sql_query: The query to be executed.
        :param arg: The arguments to pass into the query
        :return: pandas.DataFrame with query result
        """
        return pd.read_sql(sql_query, self.conn, params=arg)

    def close_connection(self) -> None:
        """
        Closes the connection with the database
        """
        self.conn.close()
        logger.debug("Connection Close")
