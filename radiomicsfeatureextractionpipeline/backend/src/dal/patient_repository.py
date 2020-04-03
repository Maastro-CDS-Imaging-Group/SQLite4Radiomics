"""
This module is used as a template for all PatientRepository.
All PatientRepositories in the data access layer should inherit from the class.
Inherits the Repository class.
"""

from abc import abstractmethod
from typing import List, Optional

from dal.database_connector import DatabaseConnector
from dal.repository import Repository
from logic.entities.patient import Patient


class PatientRepository(Repository):
    """
    This class is a template for the repository that handles all the loading and saving of patients.
    """

    def __init__(self, database_connector: DatabaseConnector, queries_file_directory: str) -> None:
        """
        Constructor for the PatientRepository class.
        :param database_connector: The database connector that will communicate with the database.
        :param queries_file_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, queries_file_directory)

    @abstractmethod
    def get_all_patients(self) -> List[Patient]:
        """
        Gets all the patients from the database
        :return: List of all patients in the database.
        """
        pass

    @abstractmethod
    def get_patient_by_id(self, patient_id: str) -> Optional[Patient]:
        """
        Gets the patients corresponding to the id.
        :param patient_id: The identifier of the patient.
        :return: The patient object that corresponds to the identifier. If no patient is found it returns None.
        """
        pass
