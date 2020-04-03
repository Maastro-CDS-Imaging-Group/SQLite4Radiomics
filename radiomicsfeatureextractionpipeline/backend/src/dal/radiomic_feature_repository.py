"""
This module is used as a template for all RadiomicFeatureRepositories.
All RadiomicFeatureRepositories in the data access layer should inherit from this class.
Inherits the Repository class.
"""
from abc import abstractmethod

from dal.database_connector import DatabaseConnector
from dal.patient_repository import PatientRepository
from dal.repository import Repository
from dal.series_repository import SeriesRepository
from logic.entities.patient import Patient
from logic.entities.radiomic_calculation import RadiomicCalculation
from logic.entities.radiomic_class import RadiomicClass
from logic.entities.radiomic_feature import RadiomicFeature
from logic.entities.radiomic_feature_value import RadiomicFeatureValue
from logic.entities.radiomic_filter import RadiomicFilter
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class RadiomicFeatureRepository(Repository):
    """
    This class is a template for the repository that handles all the loading and saving of radiomic features.
    """

    def __init__(self, database_connector: DatabaseConnector, patient_repos: PatientRepository,
                 series_repos: SeriesRepository, queries_file_directory: str) -> None:
        """
        Constructor for the RadiomicFeatureRepository class.
        :param database_connector: The database connector that will communicate with the database.
        :param patient_repos: The repository that handles all the loading and saving of patients.
        :param series_repos: The repository that handles all the loading and saving of series.
        :param queries_file_directory:The directory of the SQL-files.
        """
        super().__init__(database_connector, queries_file_directory)
        self.patient_repos: PatientRepository = patient_repos
        self.series_repos: SeriesRepository = series_repos

    @abstractmethod
    def get_radiomic_filter_by_name(self, name: str) -> RadiomicFilter:
        """
        Gets the RadiomicFilter object corresponding to the given name.
        :param name: The name of the RadiomicFilter.
        :return: The RadiomicFilter object that corresponds to the given name.
        """
        pass

    @abstractmethod
    def get_radiomic_feature_by_name(self, name: str) -> RadiomicFeature:
        """
        Gets the RadiomicFeature object corresponding to the given name.
        :param name: The name of the RadiomicFeature.
        :return: The RadiomicFeature object that corresponds to the given name.
        """
        pass

    @abstractmethod
    def get_radiomic_class_by_name(self, name: str) -> RadiomicClass:
        """
        Gets the RadiomicClass object corresponding to the given name.
        :param name: The name of the RadiomicClass.
        :return: The RadiomicClass object that corresponds to the given name.
        """
        pass

    @abstractmethod
    def get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices(
            self, patient: Patient, rtstruct_series: RtstructSeries, series_with_image_slices: SeriesWithImageSlices):
        """
        Gets the RadiomicCalculation object corresponding to the patient, rtstruct_series and ct_series.
        :param patient: The Patient is of the RadiomicCalculation
        :param rtstruct_series: The RtstructSeries of the RadiomicCalculation.
        :param series_with_image_slices: The CtSeries of the RadiomicCalculation.
        :return: The RadiomicCalculation object that corresponds to the given Patient, rtstruct_series and ct_series.
        """
        pass

    @abstractmethod
    def get_radiomic_calculation_result(self, radiomic_calculation_id: int) -> str:
        """
        Gets the path to a generated csv file with all the radiomic features of a calculation of the given identity.
        :param radiomic_calculation_id: The identity of the radiomic calculation.
        :return: Path to csv file with all radiomic features.
        """
        pass

    @abstractmethod
    def radiomic_filter_exists(self, radiomic_filter: RadiomicFilter) -> bool:
        """
        Checks whether a RadiomicFilter exists in the database.
        :param radiomic_filter: The RadiomicFilter to check.
        :return: True if RadiomicFilter is in the database. Returns False if it isn't.
        """
        pass

    @abstractmethod
    def radiomic_feature_exists(self, radiomic_feature: RadiomicFeature) -> bool:
        """
        Checks whether a RadiomicFeature exists in the database.
        :param radiomic_feature: The RadiomicFeature to check.
        :return: True if RadiomicFeature is in the database. Returns False if it isn't
        """
        pass

    @abstractmethod
    def radiomic_class_exists(self, radiomic_class: RadiomicClass) -> bool:
        """
        Checks whether a RadiomicClass exists in the database.
        :param radiomic_class: The RadiomicClass to check.
        :return: True if RadiomicClass is in the database. Returns False if it isn't.
        """
        pass

    @abstractmethod
    def save_radiomic_feature(self, radiomic_feature: RadiomicFeature) -> None:
        """
        Saves the RadiomicFeature to the database.
        :param radiomic_feature: The RadiomicFeature to save.
        :return: The method doesn't return anything.
        """
        pass

    @abstractmethod
    def save_radiomic_filter(self, radiomic_filter: RadiomicFilter) -> None:
        """
        Saves the RadiomicFilter to the database.
        :param radiomic_filter: The RadiomicFilter to save.
        :return: The method doesn't return anything.
        """
        pass

    @abstractmethod
    def save_radiomic_class(self, radiomic_class: RadiomicClass) -> None:
        """
        Saves the RadiomicClass to the database.
        :param radiomic_class: The RadiomicClass to save.
        :return: The method doesn't return anything.
        """
        pass

    @abstractmethod
    def save_radiomic_feature_value(
            self, radiomic_calculation: RadiomicCalculation, radiomic_feature_value: RadiomicFeatureValue) -> None:
        """
        Saves the RadiomicFeatureValue to the database.
        :param radiomic_calculation: The RadiomicCalculation that the RadiomicFeatureValue belongs to.
        :param radiomic_feature_value: The RadiomicFeatureValue to save.
        :return: The method doesn't return anything
        """
        pass

    @abstractmethod
    def save_radiomic_calculation(self, radiomic_calculation: RadiomicCalculation) -> None:
        """
        Saves the RadiomicCalculation to the database.
        :param radiomic_calculation: The RadiomicCalculation to save.
        :return: The method doesn't return anything.
        """
        pass

    @abstractmethod
    def get_radiomic_class_by_id(self, radiomic_class_id) -> RadiomicClass:
        """
        Gets the RadiomicClass object corresponding to it's identifier.
        :param radiomic_class_id: The identifier of the RadiomicClass.
        :return: The RadiomicClass object that corresponds to the identifier.
        """
        pass
