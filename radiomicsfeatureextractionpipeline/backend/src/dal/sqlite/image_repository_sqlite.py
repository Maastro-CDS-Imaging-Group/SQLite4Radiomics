"""
This module handles the loading and saving of images.
It inherits from the ImageRepository class.
"""

from typing import List, Tuple, Optional, Dict, Any, Callable

import pandas as pd

from dal.database_connector import DatabaseConnector
from dal.image_repository import ImageRepository
from dal.patient_repository import PatientRepository
from dal.series_repository import SeriesRepository
from dal.study_repository import StudyRepository
from logic.entities.image import Image
from logic.entities.patient import Patient
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series import Series
from logic.entities.series_with_image_slices import SeriesWithImageSlices
from logic.entities.study import Study


class ImageRepositorySqlite(ImageRepository):
    """
    Handles all transaction to the database regarding Image objects.
    """

    def __init__(self, database_connector: DatabaseConnector, series_repos: SeriesRepository,
                 patient_repos: PatientRepository, study_repos: StudyRepository,
                 query_directory: str) -> None:
        """
        Constructor for the ImageRepositorySqlite class.
        :param database_connector: The database connector that will communicate with the database.
        :param series_repos: The repository that handles all the loading and saving of series.
        :param patient_repos: The repository that handles all the loading and saving of patients.
        :param study_repos: The repository that handles all the loading and saving of studies.
        :param query_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, series_repos, patient_repos, study_repos, query_directory)

    def get_all_images_of_series(self, series: Series) -> List[Image]:
        """
        Retrieves all images from a series.
        :param series: The series to retrieve the images from.
        :return: List of all images in a series.
        """

        sql_file_path: str = r"{0}\image\get_all_images_of_series.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'series_id': series.identity}
        record_to_image_converter: Callable[[pd.Series], Image] = self.__query_result_record_to_image

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_image_converter)

    def get_image_by_id(self, image_id: str) -> Optional[Image]:
        """
        Gets the Image object corresponding to it's identifier.
        :param image_id: The identifier of the image.
        :return: The Image object that corresponds to the identifier.
        """

        sql_file_path: str = r"{0}\image\get_image_by_id.sql".format(self.query_file_directory)
        sql_parameter: Dict[str, Any] = {'image_id': image_id}
        record_to_image_converter: Callable[[pd.Series], Image] = self.__query_result_record_to_image

        return self.get_single_object_by_constrained(sql_file_path, sql_parameter, record_to_image_converter)

    def get_images_of_patients_last_ct_series_matching_rtstruct(self, sop_instance: str) \
            -> List[Tuple[Patient, RtstructSeries, SeriesWithImageSlices]]:
        """
        Gets all patient data that is connected to the SOP-Instance of an RTSTRUCT File.
        :param sop_instance: The SOP-Instance of the RTSTRUCT.
        :return: A List of Tuples with the Patient, the Rtstruct Series and the CT or PET Series.
        """

        # Gets query from SQL-file.
        query: str = self.read_sql_file(
            r'{0}\image\get_images_of_patients_last_ct_series_matching_rtstruct.sql'.format(
                self.query_file_directory))
        # Opens a connection with the database.
        with self.database_connector as db_connector:
            # Executes query and stores result in query_result.
            query_result: pd.DataFrame = db_connector.execute_query(query, {'image_id': sop_instance})
            # Connection with the database will be closed after this point.

        # Convert each image from the image_slice_id column to an Image object.
        query_result['image_slice']: Image = [self.get_image_by_file_path(x) for x in query_result['image_slice_id']]

        # Convert the rtstruct_file to an Image object.
        query_result['rtstruct']: Image = [self.get_image_by_file_path(x) for x in query_result['rtstruct_file']]

        # Convert the rtstruct_series_id to a RTSTRUCT-series object.
        query_result['rtstruct_series']: RtstructSeries = [self.series_repos.get_series_from_id(x) for x
                                                           in query_result['rtstruct_series_id']]

        # Convert the series_of_slices_id to SeriesWithImageSlices object.
        query_result['series_of_image_slices']: SeriesWithImageSlices = [self.series_repos.get_series_from_id(x) for x
                                                                         in query_result['series_of_slices_id']]

        # Convert the study_id to Study object.
        query_result['study']: Study = [self.study_repos.get_study_by_id(x) for x
                                        in query_result['study_id']]

        # Convert the patient_id to Patient object.
        query_result['patient']: Patient = [self.patient_repos.get_patient_by_id(x) for x
                                            in query_result['patient_id']]

        # Get a list of all unique series_identifiers.
        series_ids: str = query_result['series_of_slices_id'].unique()

        series_instance: str
        # Loop through all unique series identifiers.
        for series_instance in series_ids:
            # Create a list with all images that belongs to one a SeriesWithImageSlices object.
            images: List[Image] = query_result.loc[query_result['series_of_slices_id'] ==
                                                   series_instance]['image_slice'].tolist()
            # Get the SeriesWithImageSlices object that corresponds to the series instance.
            series_with_image_slices: SeriesWithImageSlices = query_result.loc[
                query_result['series_of_slices_id'] == series_instance]['series_of_image_slices'].iloc[0]

            # Adds the list of images to the SeriesWithImageSlices object.
            series_with_image_slices.images: List[Image] = images

        # Drop all columns that contain ids and the column with the image_slices and get rid of all duplicate rows.
        query_result: pd.DataFrame = query_result[['patient', 'study', 'rtstruct_series', 'rtstruct',
                                                   'series_of_image_slices']].drop_duplicates()

        # Create an empty list that will store the Patient, RtstructSeries and SeriesWithImageSlices.
        result: List[Tuple[Patient, RtstructSeries, SeriesWithImageSlices]] = []

        index: int
        record: pd.Series
        # Loop through all rows in the remaining results of the queries.
        for index, record in query_result.iterrows():
            # Add the Image of the RTSTRUCT to the RTSTRUCT-series.
            record['rtstruct_series'].image = record['rtstruct']
            # Add RTSTRUCT-series to study.
            record['study'].add_series(record['rtstruct_series'])
            # Add SeriesWithImageSlices to study.
            record['study'].add_series(record['series_of_image_slices'])
            # Add Study to Patient.
            record['patient'].add_study(record['study'])
            # Add Tuple of Patient, RTSTRUCT-series and SeriesWithImageSlices.
            result.append((record['patient'], record['rtstruct_series'], record['series_of_image_slices']))

        return result

    def get_image_by_file_path(self, file_path: str) -> Optional[Image]:
        """
        Gets the Image object corresponding to the file path.
        :param file_path: The file path of the image.
        :return: The Image object that corresponds to the file path.
        """

        sql_file_path: str = r"{0}\image\get_image_by_file_path.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'object_file': file_path}
        record_to_image_converter: Callable[[pd.Series], Image] = self.__query_result_record_to_image

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_image_converter)

    @staticmethod
    def __query_result_record_to_image(record: pd.Series) -> Image:
        """
        Converts record in DICOMImage table to Image object.
        :param record: One record of the table returned by the database.
        :return: Image object created with the data in the record.
        """

        instance: str = record['SOPInstanc']
        class_ui: str = record['SOPClassUI']
        number: str = record['ImageNumbe']
        date: str = record['ImageDate']
        time: str = record['ImageTime']
        echo_number: str = record['EchoNumber']
        number_of_frames: str = record['NumberOfFr']
        acq_date: str = record['AcqDate']
        acq_time: str = record['AcqTime']
        receiving_c: str = record['ReceivingC']
        acq_number: str = record['AcqNumber']
        slice_location: str = record['SliceLocat']
        samples_per: str = record['SamplesPer']
        photo_metric: str = record['PhotoMetri']
        rows: str = record['Rows']
        columns: str = record['Colums']
        bits_stored: str = record['BitsStored']
        image_type: str = record['ImageType']
        identity: str = record['ImageID']
        object_file: str = record['ObjectFile']
        device_name: str = record['DeviceName']

        # Create image object from table row.
        return Image(instance, class_ui, number, date, time, echo_number, number_of_frames, acq_date, acq_time,
                     receiving_c, acq_number, slice_location, samples_per, photo_metric, rows, columns, bits_stored,
                     image_type, identity, object_file, device_name)
