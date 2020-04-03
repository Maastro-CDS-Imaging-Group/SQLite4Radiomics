"""
This module is used as a template for all ImageRepositories.
All ImageRepositories in the data access layer should inherit from this class.
Inherits the Repository class.
"""

from abc import abstractmethod
from typing import List, Tuple, Optional

from dal.database_connector import DatabaseConnector
from dal.patient_repository import PatientRepository
from dal.repository import Repository
from dal.series_repository import SeriesRepository
from dal.study_repository import StudyRepository
from logic.entities.image import Image
from logic.entities.patient import Patient
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series import Series
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class ImageRepository(Repository):
    """
    This class is a template for the repository that handles all the loading and saving of images.
    """

    def __init__(self, database_connector: DatabaseConnector, series_repos: SeriesRepository,
                 patient_repos: PatientRepository, study_repos: StudyRepository,
                 queries_file_directory: str) -> None:
        """
        Constructor for the ImageRepository class.
        :param database_connector: The database connector that will communicate with the database.
        :param series_repos: The repository that handles all the loading and saving of series.
        :param patient_repos: The repository that handles all the loading and saving of patients.
        :param study_repos: The repository that handles all the loading and saving of studies.
        :param queries_file_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, queries_file_directory)
        self.series_repos: SeriesRepository = series_repos
        self.patient_repos: PatientRepository = patient_repos
        self.study_repos: StudyRepository = study_repos

    @abstractmethod
    def get_all_images_of_series(self, series: Series) -> List[Image]:
        """
        Retrieves all images from a series.
        :param series: The series tho retrieve the images from.
        :return: List of all images in a series.
        """
        pass

    @abstractmethod
    def get_images_of_patients_last_ct_series_matching_rtstruct(
            self, sop_instance: str) -> List[Tuple[Patient, RtstructSeries, SeriesWithImageSlices]]:
        """
        Gets all patient data that is connected to the SOP-Instance of an RTSTRUCT File.
        :param sop_instance: The SOP-Instance of the RTSTRUCT.
        :return: A List of Tuples with the Patient, the Rtstruct Series and the CT or PET Series.
        """
        pass

    @abstractmethod
    def get_image_by_id(self, image_id: str) -> Optional[Image]:
        """
        Gets the Image object corresponding to it's identifier.
        :param image_id: The identifier of the image.
        :return: The Image object that corresponds to the identifier.
        """
        pass

    @abstractmethod
    def get_image_by_file_path(self, file_path: str) -> Optional[Image]:
        """
        Gets the Image object corresponding to the file path.
        :param file_path: The file path of the image.
        :return: The Image object that corresponds to the file path.
        """
        pass
