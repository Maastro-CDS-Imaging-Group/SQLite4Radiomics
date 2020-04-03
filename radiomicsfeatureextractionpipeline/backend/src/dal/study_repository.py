"""
This module is used as a template for all StudyRepositories.
All StudyRepositories in the data access layer should inherit from this class.
Inherits the Repository class.
"""
from abc import abstractmethod
from typing import List, Optional

from dal.database_connector import DatabaseConnector
from dal.repository import Repository
from logic.entities.study import Study


class StudyRepository(Repository):
    """
    This class is a template for the repository that handles all the loading and saving of studies.
    """

    def __init__(self, database_connector: DatabaseConnector, queries_file_directory: str) -> None:
        """
        Constructor for the StudyRepository class.
        :param database_connector: The database connector that will communicate with the database.
        :param queries_file_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, queries_file_directory)

    @abstractmethod
    def get_all_studies(self) -> List[Study]:
        """
        Gets a list of all studies in the database.
        :return: A list of all studies in the database.
        """
        pass

    @abstractmethod
    def get_study_by_id(self, study_id: str) -> Optional[Study]:
        """
        Gets the Study object corresponding to it's identifier.
        :param study_id: The identifier of the Study
        :return: The Study object that corresponds to the identifier.
        """
        pass
