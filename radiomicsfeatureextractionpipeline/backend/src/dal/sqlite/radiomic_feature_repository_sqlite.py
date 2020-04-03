"""
This module handles the loading and saving of the radiomic features.
It inherits from the RadiomicFeatureRepository class.
"""

import datetime
import os
from typing import Optional, Any, Dict, Callable

import pandas as pd

from dal.database_connector import DatabaseConnector
from dal.database_error import DatabaseError
from dal.patient_repository import PatientRepository
from dal.radiomic_feature_repository import RadiomicFeatureRepository
from dal.series_repository import SeriesRepository
from logic.entities.patient import Patient
from logic.entities.radiomic_calculation import RadiomicCalculation
from logic.entities.radiomic_class import RadiomicClass
from logic.entities.radiomic_feature import RadiomicFeature
from logic.entities.radiomic_feature_value import RadiomicFeatureValue
from logic.entities.radiomic_filter import RadiomicFilter
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class RadiomicFeatureRepositorySqlite(RadiomicFeatureRepository):
    """
    Handles all transaction to the database regarding RadiomicCalculation, RadiomicClass, RadiomicFilter,
    RadiomicFeature, RadiomicFeatureValue classes.
    """

    def __init__(self, database_connector: DatabaseConnector, patient_repos: PatientRepository,
                 series_repos: SeriesRepository, query_directory: str, type_of_save: str) -> None:
        """
        Constructor for the RadiomicFeatureRepositorySQL.
        :param database_connector: The database connector that will communicate with the database.
        :param patient_repos: The repository that handles all the loading and saving of patients.
        :param series_repos: The repository that handles all the loading and saving of series.
        :param query_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, patient_repos, series_repos, query_directory)

        self.save_method: str = type_of_save
        print(self.save_method)

    def save_radiomic_feature(self, radiomic_feature: RadiomicFeature) -> None:
        """
        Saves the RadiomicFeature to the database.
        :param radiomic_feature: The RadiomicFeature to save.
        :return: The method doesn't return anything.
        """

        sql_file_path: str = r"{0}\radiomics\save_radiomic_feature.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'class_id': int(radiomic_feature.radiomic_class.identity),
                                          'name': radiomic_feature.name}
        radiomic_feature_exist_checker: Callable[[RadiomicFeature], bool] = self.radiomic_feature_exists
        radiomic_feature_to_save: RadiomicFeature = radiomic_feature

        self.save_object(sql_file_path, sql_parameters, radiomic_feature_exist_checker, radiomic_feature_to_save)

    def save_radiomic_filter(self, radiomic_filter: RadiomicFilter) -> None:
        """
        Saves the RadiomicFilter to the database.
        :param radiomic_filter: The RadiomicFilter to save.
        :return: The method doesn't return anything.
        """

        sql_file_path: str = r"{0}\radiomics\save_radiomic_filter.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': radiomic_filter.name}
        radiomic_filter_exist_checker: Callable[[RadiomicFilter], bool] = self.radiomic_filter_exists
        radiomic_filter_to_save: RadiomicFilter = radiomic_filter

        self.save_object(sql_file_path, sql_parameters, radiomic_filter_exist_checker, radiomic_filter_to_save)

    def save_radiomic_class(self, radiomic_class: RadiomicClass) -> None:
        """
        Saves the RadiomicClass to the database.
        :param radiomic_class: The RadiomicClass to save.
        :return: The method doesn't return anything.
        """

        sql_file_path: str = r"{0}\radiomics\save_radiomic_class.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': radiomic_class.name}
        radiomic_class_exist_checker: Callable[[RadiomicClass], bool] = self.radiomic_class_exists
        radiomic_class_to_save: RadiomicClass = radiomic_class

        self.save_object(sql_file_path, sql_parameters, radiomic_class_exist_checker, radiomic_class_to_save)

    def save_radiomic_feature_value(self, radiomic_calculation: RadiomicCalculation,
                                    radiomic_feature_value: RadiomicFeatureValue) -> None:
        """
        Saves the RadiomicFeatureValue to the database.
        :param radiomic_calculation: The RadiomicCalculation that the RadiomicFeatureValue belongs to.
        :param radiomic_feature_value: The RadiomicFeatureValue to save.
        :return: The method doesn't return anything
        """

        sql_file_path = r"{0}\radiomics\save_radiomic_feature_value.sql".format(self.query_file_directory)
        sql_parameters = {'radiomics_id': int(radiomic_calculation.identity),
                          'roi_id': int(radiomic_feature_value.roi.identity),
                          'filter_id': int(radiomic_feature_value.radiomic_filter.identity),
                          'class_id': int(radiomic_feature_value.radiomic_class.identity),
                          'feature_id': int(radiomic_feature_value.feature.identity),
                          'value': str(radiomic_feature_value.value)}
        radiomic_feature_value_exist_checker: Callable[
            [RadiomicFeatureValue], bool] = self.radiomic_feature_value_exists
        radiomic_feature_value_to_save: RadiomicFeatureValue = radiomic_feature_value
        radiomic_calculation_of_feature_value: RadiomicCalculation = radiomic_calculation

        self.save_object(sql_file_path, sql_parameters, radiomic_feature_value_exist_checker,
                         radiomic_feature_value_to_save, radiomic_calculation)

    def save_radiomic_calculation(self, radiomic_calculation: RadiomicCalculation) -> None:
        """
        Saves the RadiomicCalculation to the database.
        :param radiomic_calculation: The RadiomicCalculation to save.
        :return: The method doesn't return anything.
        """

        sql_file_path: str = r"{0}\radiomics\save_radiomic_calculation.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = \
            {'patient_id': radiomic_calculation.patient.identity,
             'series_images_slices_modality': radiomic_calculation.series_with_image_slices.modality,
             'series_image_slices_id': radiomic_calculation.series_with_image_slices.identity,
             'rtstruct_series_id': radiomic_calculation.rtstruct_series.identity,
             'time': radiomic_calculation.time}
        radiomic_calculation_exist_checker: Callable[[RadiomicCalculation], bool] = self.radiomic_calculation_exists
        radiomic_calculation_to_save: RadiomicCalculation = radiomic_calculation

        self.save_object(sql_file_path, sql_parameters, radiomic_calculation_exist_checker,
                         radiomic_calculation_to_save)

    def radiomic_feature_exists(self, radiomic_feature: RadiomicFeature) -> bool:
        """
        Checks whether a RadiomicFeature exists in the database.
        :param radiomic_feature: The RadiomicFeature to check.
        :return: True if RadiomicFeature is in the database. Returns False if it isn't
        """

        sql_file_path: str = r"{0}\radiomics\radiomic_feature_exists.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': radiomic_feature.name}

        return self.check_if_object_exist_in_database(sql_file_path, sql_parameters)

    def radiomic_filter_exists(self, radiomic_filter: RadiomicFilter) -> bool:
        """
        Checks whether a RadiomicFilter exists in the database.
        :param radiomic_filter: The RadiomicFilter to check.
        :return: True if RadiomicFilter is in the database. Returns False if it isn't.
        """

        sql_file_path: str = r"{0}\radiomics\radiomic_filter_exists.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': radiomic_filter.name}

        return self.check_if_object_exist_in_database(sql_file_path, sql_parameters)

    def radiomic_class_exists(self, radiomic_class: RadiomicClass) -> bool:
        """
        Checks whether a RadiomicClass exists in the database.
        :param radiomic_class: The RadiomicClass to check.
        :return: True if RadiomicClass is in the database. Returns False if it isn't.
        """

        sql_file_path: str = r"{0}\radiomics\radiomic_class_exists.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': radiomic_class.name}

        return self.check_if_object_exist_in_database(sql_file_path, sql_parameters)

    def radiomic_feature_value_exists(self, radiomic_feature_value: RadiomicFeatureValue,
                                      radiomic_calculation: RadiomicCalculation) -> bool:
        """
        Checks whether a RadiomicFeatureValue exists in the database.
        :param radiomic_feature_value: The RadiomicFeatureValue to check.
        :param radiomic_calculation: The RadiomicCalculation of the RadiomicFeatureValue.
        :return: Returns True if RadiomicFeatureValue exists in the database. Returns False if it isn't.
        """

        sql_file_path: str = r"{0}\radiomics\radiomic_feature_value_exists.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'radiomics_id': radiomic_calculation.identity,
                                          'roi_id': radiomic_feature_value.roi.identity,
                                          'radiomic_filter_id': radiomic_feature_value.radiomic_filter.identity,
                                          'radiomic_class_id': radiomic_feature_value.radiomic_class.identity,
                                          'radiomic_feature_id': radiomic_feature_value.feature.identity}

        return self.check_if_object_exist_in_database(sql_file_path, sql_parameters)

    def radiomic_calculation_exists(self, radiomic_calculation: RadiomicCalculation):
        """
        Checks whether a RadiomicCalculation exists in the database.
        :param radiomic_calculation: The RadiomicCalculation to check.
        :return: Returns True if RadiomicCalculation exists in the database. Returns False if it isn't.
        """

        sql_file_path: str = r"{0}\radiomics\radiomic_calculation_exists.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {
            'patient_id': radiomic_calculation.patient.identity,
            'series_with_image_slices_modality': radiomic_calculation.series_with_image_slices.modality,
            'series_with_image_slices_id': radiomic_calculation.series_with_image_slices.identity,
            'rtstruct_series_id': radiomic_calculation.rtstruct_series.identity,
            'time_of_calculation': radiomic_calculation.time}

        return self.check_if_object_exist_in_database(sql_file_path, sql_parameters)

    def get_radiomic_calculation_by_patient_rtstruct_and_series_with_image_slices(
            self, patient: Patient, rtstruct_series: RtstructSeries,
            series_with_image_slices: SeriesWithImageSlices) -> RadiomicCalculation:
        """
        Gets the RadiomicCalculation object corresponding to the patient, rtstruct_series and ct_series.
        :param patient: The Patient of the RadiomicCalculation
        :param rtstruct_series: The RtstructSeries of the RadiomicCalculation.
        :param series_with_image_slices: The CtSeries of the RadiomicCalculation.
        :return: The RadiomicCalculation object that corresponds to the given Patient, rtstruct_series and ct_series.
        """

        sql_file_path: str = r"{0}\radiomics\get_radiomic_calculation.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'patient_id': patient.identity,
                                          'rtstruct_series_id': rtstruct_series.identity,
                                          'series_image_slices_id': series_with_image_slices.identity}
        record_to_radiomic_calculation_converter: Callable[
            [pd.Series], RadiomicCalculation] = self.__query_result_to_radiomic_calculation

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters,
                                                     record_to_radiomic_calculation_converter, True)

    def get_radiomic_filter_by_name(self, name: str) -> RadiomicFilter:
        """
        Gets the RadiomicFilter object corresponding to the given name.
        :param name: The name of the RadiomicFilter.
        :return: The RadiomicFilter object that corresponds to the given name.
        """

        sql_file_path: str = r"{0}\radiomics\get_radiomic_filter.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'filter_name': name}
        record_to_radiomic_filter_converter: Callable[
            [pd.Series], RadiomicFilter] = self.__query_result_to_radiomic_filter

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_radiomic_filter_converter)

    def get_radiomic_feature_by_name(self, name: str) -> RadiomicFeature:
        """
        Gets the RadiomicFeature object corresponding to the given name.
        :param name: The name of the RadiomicFeature.
        :return: The RadiomicFeature object that corresponds to the given name.
        """

        sql_file_path: str = r"{0}\radiomics\get_radiomic_feature.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'feature_name': str(name)}
        record_to_radiomic_feature_converter: Callable[
            [pd.Series], RadiomicFeature] = self.__query_result_to_radiomic_feature

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters,
                                                     record_to_radiomic_feature_converter)

    def get_radiomic_class_by_name(self, name: str) -> RadiomicClass:
        """
        Gets the RadiomicClass object corresponding to the given name.
        :param name: The name of the RadiomicClass.
        :return: The RadiomicClass object that corresponds to the given name.
        """

        sql_file_path: str = r"{0}\radiomics\get_radiomic_class.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'class_name': name}
        record_to_radiomic_class_converter: Callable[[pd.Series], RadiomicClass] = self.__query_result_to_radiomic_class

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_radiomic_class_converter)

    def get_radiomic_class_by_id(self, radiomic_class_id: int) -> RadiomicClass:
        """
        Gets the RadiomicClass object corresponding to it's identifier.
        :param radiomic_class_id: The identifier of the RadiomicClass.
        :return: The RadiomicClass object that corresponds to the identifier.
        """

        sql_file_path: str = r"{0}\radiomics\get_radiomic_class_by_id.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'id': int(radiomic_class_id)}
        record_to_radiomic_class_converter: Callable[[pd.Series], RadiomicClass] = self.__query_result_to_radiomic_class

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_radiomic_class_converter)

    def get_radiomic_calculation_result(self, radiomic_calculation_id: int) -> str:
        """
        Gets the path to a generated csv file with all the radiomic features of a calculation of the given identity.
        :param radiomic_calculation_id: The identity of the radiomic calculation.
        :return: Path to csv file with all radiomic features.
        """

        sql_file_path = r"{0}\radiomics\get_radiomic_calculation_result.sql".format(self.query_file_directory)
        sql_parameters = {'radiomic_id': int(radiomic_calculation_id)}

        query_result: pd.DataFrame = self.execute_query(sql_file_path, sql_parameters)

        # Modifies query result so that all RadiomicFeatures are stored in columns rather than rows.
        query_result: pd.DataFrame = query_result.pivot_table(
            index=['Patient Id', 'Modality Image Slices Series', 'CT or PET series instance',
                   'Rtstruct series instance', 'Roi name', 'Time of calculation'],
            columns='Feature', values='Value', aggfunc='first').reset_index()

        # Gets returned patient_id
        patient_id: str = query_result.iloc[0]['Patient Id']

        # Gets returned modality for the series with image slices
        modality: str = query_result.iloc[0]['Modality Image Slices Series']

        # Sets the file path where the CSV will be stored.
        if self.save_method == 'dump':
            file_path_to_csv: str = r"out\data.csv"  # saves all data from the database into one file
        elif self.save_method == 'individual':
            file_path_to_csv: str = r"out\{0}\{0} {1}.csv".format(patient_id, modality) # save csv per patient and modality

        # Creates CSV-file with all it's directories.
        dir_path: str = os.path.dirname(file_path_to_csv)
        if not os.path.isdir(r'out'):
            os.mkdir(r'out')
        if not os.path.isdir(dir_path):
            os.mkdir(dir_path)
        if not os.path.exists(file_path_to_csv):
            open(file_path_to_csv, 'x')
        else:
            # If csv already exists then new data will be appended to the old.
            previous_results: pd.DataFrame = pd.read_csv(file_path_to_csv)
            query_result: pd.DataFrame = previous_results.append(query_result)

        # Saves the CSV-file
        query_result.to_csv(file_path_to_csv, index=False)

        # Returns the path to the CSV-file
        return file_path_to_csv


    def __query_result_to_radiomic_calculation(self, record: pd.Series) -> RadiomicCalculation:
        """
        Converts record in DICOMRadiomics table to RadiomicCalculation object.
        :param record: One record of the table returned by the database.
        :return: RadiomicCalculation object created with the data in the record.
        """

        identity: int = record['RadiomicsId']
        patient: Patient = self.patient_repos.get_patient_by_id(record["RadiomicPat"])
        rtstruct_series: Optional[RtstructSeries] = self.series_repos.get_series_from_id(
            record["RadiomicRtstructSeries"])
        series_with_image_slices: Optional[SeriesWithImageSlices] = self.series_repos.get_series_from_id(
            record["RadiomicSeriesOfImageSlices"])
        time_of_calculation: datetime.datetime = record['TimeOfCalculation']

        # Checks whether rtstruct_series was actually a RTSTRUCT-series.
        if not isinstance(rtstruct_series, RtstructSeries):
            raise DatabaseError("Error occurred while loading the data!")

        # Checks whether series_with_image_slices was actually a SeriesWithImageSlices.
        if not isinstance(series_with_image_slices, SeriesWithImageSlices):
            raise DatabaseError("Error occurred while loading the data!")

        # Create RadiomicCalculation object from table row.
        return RadiomicCalculation(patient, rtstruct_series, series_with_image_slices, time_of_calculation, identity)

    def __query_result_to_radiomic_filter(self, record: pd.Series) -> RadiomicFilter:
        """
        Converts record in DICOMRadiomicFilter table to RadiomicFilter object.
        :param record: One record of the table returned by the database.
        :return: RadiomicFilter object created with the data in the record.
        """

        identity: int = record['FilterId']
        name: str = record['Name']

        # Create RadiomicFilter object from table row.
        return RadiomicFilter(name, identity)

    def __query_result_to_radiomic_feature(self, record: pd.Series) -> RadiomicFeature:
        """
        Converts record in DICOMRadiomicFeature table to RadiomicFeature object.
        :param record: One record of the table returned by the database.
        :return: RadiomicFeature object created with the data in the record.
        """

        identity: int = record['RadiomicFeatureId']
        radiomic_class: RadiomicClass = self.get_radiomic_class_by_id(record['RadiomicClassId'])
        name: str = record['Name']

        # Create RadiomicFeature object from table row.
        return RadiomicFeature(radiomic_class, name, identity)

    def __query_result_to_radiomic_class(self, record: pd.Series) -> RadiomicClass:
        """
        Converts record in DICOMRadiomicClass table to RadiomicClass object.
        :param record: One record of the table returned by the database.
        :return: RadiomicClass object created with the data in the record.
        """
        identity: int = record['ClassId']
        parent_identity: int = record['ParentClassId']
        parent_class: Optional[RadiomicClass] = None

        # Checks whether RadiomicClass has parent class.
        if parent_identity is not None:
            # Loads parent class object.
            parent_class: Optional[RadiomicClass] = self.get_radiomic_class_by_id(parent_identity)
        name: str = record['Name']

        # Create RadiomicClass object from table row.
        return RadiomicClass(name, identity, parent_class)