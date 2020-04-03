"""
This module handles the loading and saving of series.
It inherits from the SeriesRepository class.
"""

from typing import List, Optional, Any, Dict, Callable

import pandas as pd

from dal.database_connector import DatabaseConnector
from dal.series_repository import SeriesRepository
from logic.entities.ct_series import CtSeries
from logic.entities.patient import Patient
from logic.entities.pet_series import PetSeries
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series import Series
from logic.entities.study import Study
from logic.entities.mri_series import MriSeries


class SeriesRepositorySqlite(SeriesRepository):
    """
    Handles all transaction to the database regarding Series objects.
    """

    def __init__(self, database_connector: DatabaseConnector, query_directory: str) -> None:
        """
        Constructor for the SeriesRepositorySqlite class.
        :param database_connector: The database connector that will communicate with the database.
        :param query_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, query_directory)
    
    def get_all_series(self) -> List[Series]:
        """
        Gets a list of all the stored series in the database.
        :return: A list of all the stored series in the database.
        """

        sql_file_path: str = r"{0}\series\get_all_series.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {}
        record_to_patient_converter: Callable[[pd.Series], Series] = self.__query_result_to_series

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)

    def get_all_series_of_modality_type(self, modality: str) -> List[Series]:
        """
        Gets a list of all the stored series in the database with a given modality.
        :param modality: The modality to filter the series with.
        :return: A filtered list of series stored in the database.
        """

        sql_file_path: str = r"{0}\series\get_all_series_of_modality.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'modality': modality}
        record_to_patient_converter: Callable[[pd.Series], Series] = self.__query_result_to_series

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)
        
    def get_all_series_from_study(self, study: Study) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given study.
        :param study: The study to filter the series with.
        :return: A filtered list of series stored in the database.
        """

        sql_file_path: str = r"{0}\series\get_all_series_from_study.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'study_id': study.identity}
        record_to_patient_converter: Callable[[pd.Series], Series] = self.__query_result_to_series

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)
        
    def get_all_series_from_study_of_modality_type(self, study: Study, modality: str) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given study with a given modality.
        :param study: The study to filter the series with.
        :param modality: The modality to filter the series with.
        :return: A filtered list of series stored in the database.
        """

        sql_file_path: str = r"{0}\series\get_all_series_from_study_of_modality_type.sql".format(
            self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'study_id': study.identity, 'modality': modality}
        record_to_patient_converter: Callable[[pd.Series], Series] = self.__query_result_to_series

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)
        
    def get_all_series_from_patient(self, patient: Patient) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given patient.
        :param patient: The patient to filter the series with.
        :return: A filtered list of series stored in the database.
        """

        sql_file_path: str = r"{0}\series\get_all_series_from_patient.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'patient_id': patient.identity}
        record_to_patient_converter: Callable[[pd.Series], Series] = self.__query_result_to_series

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)
        
    def get_all_series_from_patient_of_modality_type(self, patient: Patient, modality: str) -> List[Series]:
        """
        Gets a list of all the stored series in the database that belong to the given patient with a given modality.
        :param patient: The patient to filter the series with.
        :param modality: The modality to filter the series with.
        :return: A filtered list of series stored in the database.
        """

        sql_file_path: str = r"{0}\series\get_all_series_from_patient_of_modality_type.sql".format(
            self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'patient_id': patient.identity, 'modality': modality}
        record_to_patient_converter: Callable[[pd.Series], Series] = self.__query_result_to_series

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)

    def get_series_from_id(self, series_id: str) -> Optional[Series]:
        """
        Gets the series object corresponding to it's identifier.
        :param series_id: The identifier of the Series.
        :return: The Series object that corresponds to the identifier.
        """

        sql_file_path: str = r"{0}\series\get_series_from_id.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'series_id': str(series_id)}
        record_to_series_converter: Callable[[pd.Series], Series] = self.__query_result_to_series

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_series_converter)

    @staticmethod
    def __query_result_to_series(record: pd.Series) -> Series:
        """
        Converts record in DICOMSeries table to Series object.
        :param record: One record of the table returned by the database.
        :return: Series object created with the data in the record.
        """
        identity: str = record['SeriesInst']
        number: str = record['SeriesNumb']
        modality: str = record['Modality']
        manufacture: str = record['Manufactur']
        model_name: str = record['ModelName']
        patient_position: str = record['PatientPos']

        # Checks whether series is a RTSTRUCT-series.
        if record['Modality'] == 'RTSTRUCT':
            # Create RtstructSeries object from table row.
            return RtstructSeries(identity, number, modality, manufacture, model_name, patient_position)

        date: str = record['SeriesDate']
        time: str = record['SeriesTime']
        description: str = record['SeriesDesc']
        body_part_ex: str = record['BodyPartEx']
        protocol_name: str = record['ProtocolNa']
        institution: str = record['Institutio']
        frame_of_reference: str = record['FrameOfRef']

        # Checks whether series is a CT-series.
        if modality == 'CT':
            # Create CTSeries object from table row.
            return CtSeries(identity, number, modality, manufacture, model_name, patient_position, date, time,
                            description, body_part_ex, protocol_name, institution, frame_of_reference)

        # Checks wheter series is a PET-series
        if modality == 'PT':
            # Create PetSeries object from table row.
            return PetSeries(identity, number, modality, manufacture, model_name, patient_position, date, time,
                             description, body_part_ex, protocol_name, institution, frame_of_reference)

        # Checks whether series is a MRI-series
        if modality == 'MR':
            # Create MrSeries object from table row.
            return MriSeries(identity, number, modality, manufacture, model_name, patient_position, date, time,
                             description, body_part_ex, protocol_name, institution, frame_of_reference)