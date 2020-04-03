"""
This module is used as a template for all SeriesRepositories.
All SeriesRepositories in the data access layer should inherit from this class.
Inherits the Repository class.
"""

from abc import abstractmethod
from typing import List, Optional

from dal.database_connector import DatabaseConnector
from dal.repository import Repository
from logic.entities.patient import Patient
from logic.entities.series import Series
from logic.entities.study import Study


class SeriesRepository(Repository):
    """
    This class is a template for the repository that handles all the loading and saving of series.
    """

    def __init__(self, database_connector: DatabaseConnector, queries_file_directory: str) -> None:
        """
        Constructor for the SeriesRepository class.
        :param database_connector: The database connector that will communicate with the database.
        :param queries_file_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, queries_file_directory)

    @abstractmethod
    def get_all_series(self) -> List[Series]:
        """
        Gets a list of all the stored series in the database.
        :return: A list of all the stored series in the database.
        """
        pass

    @abstractmethod
    def get_all_series_from_study(self, study: Study) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given study.
        :param study: The study to filter the series with.
        :return: A filtered list of series stored in the database.
        """
        pass

    @abstractmethod
    def get_all_series_from_study_of_modality_type(self, study: Study, modality: str) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given study with a given modality.
        :param study: The study to filter the series with.
        :param modality: The modality to filter the series with.
        :return: A filtered list of series stored in the database.
        """
        pass

    @abstractmethod
    def get_all_series_from_patient(self, patient: Patient) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given patient.
        :param patient: The patient to filter the series with.
        :return: A filtered list of series stored in the database.
        """
        pass

    @abstractmethod
    def get_all_series_from_patient_of_modality_type(self, patient: Patient, modality: str) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given patient with a given modality.
        :param patient: The patient to filter the series with.
        :param modality: The modality to filter the series with.
        :return: A filtered list of series stored in the database.
        """
        pass

    @abstractmethod
    def get_all_series_of_modality_type(self, modality: str) -> List[Series]:
        """
        Gets a list of all the stored series in the database with a given modality.
        :param modality: The modality to filter the series with.
        :return: A filtered list of series stored in the database.
        """
        pass

    @abstractmethod
    def get_series_from_id(self, series_id: str) -> Optional[Series]:
        """
        Gets the series object corresponding to it's identifier.
        :param series_id: The identifier of the Series.
        :return: The Series object that corresponds to the identifier.
        """
        pass
