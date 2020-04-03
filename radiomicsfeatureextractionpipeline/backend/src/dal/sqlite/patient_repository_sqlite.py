"""
This module handles the loading and saving of patients.
It inherits from the PatientRepository class.
"""

from typing import List, Optional, Dict, Any, Callable

import pandas as pd

from dal.database_connector import DatabaseConnector
from dal.patient_repository import PatientRepository
from logic.entities.patient import Patient


class PatientRepositorySqlite(PatientRepository):
    """
    Handles all transaction to the database regarding Patient objects
    """

    def __init__(self, database_connector: DatabaseConnector, query_directory: str) -> None:
        """
        Constructor for the PatientRepositorySqlite
        :param database_connector: The database connector that will communicate with the database.
        :param query_directory: The directory of the SQL-files
        """
        super().__init__(database_connector, query_directory)
    
    def get_all_patients(self) -> List[Patient]:
        """
        Gets all the patients from the database
        :return: List of all patients int the database
        """

        sql_file_path: str = r"{0}\patient\get_all_patients.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {}
        record_to_patient_converter: Callable[[pd.Series], Patient] = self.__query_result_to_patient

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_patient_converter)
        
    def get_patient_by_id(self, patient_id: str) -> Optional[Patient]:
        """
        Gets the patients corresponding to the id.
        :param patient_id: The identifier of the patient.
        :return: The patient object that corresponds to the identifier. If no patient is found it returns None.
        """

        sql_file_path: str = r"{0}\patient\get_patient_by_id.sql".format(self.query_file_directory)
        sql_parameter: Dict[str, Any] = {'patient_id': patient_id}
        record_to_patient_converter: Callable[[pd.Series], Patient] = self.__query_result_to_patient

        return self.get_single_object_by_constrained(sql_file_path, sql_parameter, record_to_patient_converter)

    @staticmethod
    def __query_result_to_patient(record: pd.Series) -> Patient:
        """
        Converts record in DICOMPatient table to Patient object.
        :param record: One record of the table returned by the database.
        :return: Patient object created with the data in the record.
        """

        patient_id: str = record['PatientID']
        patient_name: str = record['PatientNam']
        patient_sex: str = record['PatientSex']
        access_time: str = record['AccessTime']

        # Create Patient object from table row.
        return Patient(patient_id, patient_name, patient_sex, access_time)
