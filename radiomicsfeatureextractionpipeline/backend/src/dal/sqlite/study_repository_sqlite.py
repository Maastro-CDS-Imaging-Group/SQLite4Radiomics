"""
This module handles the loading and saving of studies.
It inherits from the StudyRepository class.
"""
from typing import List, Optional, Dict, Any, Callable

import pandas as pd

from dal.database_connector import DatabaseConnector
from dal.study_repository import StudyRepository
from logic.entities.study import Study


class StudyRepositorySqlite(StudyRepository):
    """
    Handles all transaction to the database regarding Study objects
    """

    def __init__(self, database_connector: DatabaseConnector, query_directory: str) -> None:
        """
        Constructor for the StudyRepositorySqlite class.
        :param database_connector: The database connector that will communicate with the database.
        :param query_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, query_directory)

    def get_all_studies(self) -> List[Study]:
        """
        Gets a list of all studies in the database.
        :return: A list of all studies in the database.
        """

        sql_file_path: str = r"{0}\study\get_all_studies.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {}
        record_to_patient_converter: Callable[[pd.Series], Study] = self.__query_result_to_study

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)

    def get_study_by_id(self, study_id: str) -> Optional[Study]:
        """
        Gets the Study object corresponding to it's identifier.
        :param study_id: The identifier of the Study
        :return: The Study object that corresponds to the identifier.
        """

        sql_file_path: str = r"{0}\study\get_study_by_id.sql". format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'study_id': study_id}
        record_to_study_converter: Callable[[pd.Series], Study] = self.__query_result_to_study

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_study_converter)

    @staticmethod
    def __query_result_to_study(record: pd.Series) -> Study:
        """
        Converts record in DICOMStudy table to Study object
        :param record: One record of the table returned by the database.
        :return: Study object created with the data in the record.
        """

        instance: str = record['StudyInsta']
        date: str = record['StudyDate']
        time: str = record['StudyTime']
        identity: str = record['StudyID']
        description: str = record['StudyDescr']
        accession_n: str = record['AccessionN']
        refer_physicist: str = record['ReferPhysi']
        patients_ag: str = record['PatientsAg']
        patients_we: str = record['PatientsWe']
        modalities: str = record['StudyModal']

        #  Create image object from table row.
        return Study(instance, date, time, identity, description, accession_n, refer_physicist,
                     patients_ag, patients_we, modalities)
