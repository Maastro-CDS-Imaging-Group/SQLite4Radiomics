"""
This module keeps track of all Repositories in the dal.
"""

from dal.image_repository import ImageRepository
from dal.patient_repository import PatientRepository
from dal.radiomic_feature_repository import RadiomicFeatureRepository
from dal.roi_repository import ROIRepository
from dal.series_repository import SeriesRepository
from dal.study_repository import StudyRepository


class DataAccessLayer:
    """
    This class will keep track of all the instances of Repositories.
    Other classes can ask the DataAccessLayer for instances rather than instantiating classes by themselves.
    """

    def __init__(self, image_repos: ImageRepository, patient_repos: PatientRepository,
                 radiomic_feature_repos: RadiomicFeatureRepository, roi_repos: ROIRepository,
                 series_repos: SeriesRepository, study_repos: StudyRepository) -> None:
        """
        Constructor for DataAccessLayer class.
        :param image_repos: Instance of the ImageRepository class.
        :param patient_repos: Instance of the PatientRepository class.
        :param radiomic_feature_repos: Instance of the RadiomicFeatureRepository class.
        :param roi_repos: Instance of the ROIRepository class.
        :param series_repos: Instance of the SeriesRepository class.
        :param study_repos: Instance of the StudyRepository class.
        """
        self.image_repos: ImageRepository = image_repos
        self.patient_repos: PatientRepository = patient_repos
        self.radiomic_feature_repos: RadiomicFeatureRepository = radiomic_feature_repos
        self.roi_repos: ROIRepository = roi_repos
        self.series_repos: SeriesRepository = series_repos
        self.study_repos: StudyRepository = study_repos

    def get_image_repos(self) -> ImageRepository:
        """
        Returns an instance of the ImageRepository class.
        :return: Instance of the ImageRepository class.
        """
        return self.image_repos

    def get_patient_repos(self) -> PatientRepository:
        """
        Returns an instance of the PatientRepository class.
        :return: Instance of the PatientRepository class.
        """
        return self.patient_repos

    def get_radiomic_feature_repos(self) -> RadiomicFeatureRepository:
        """
        Returns an instance of the RadiomicFeatureRepository class.
        :return: Instance of the RadiomicFeatureRepository class.
        """
        return self.radiomic_feature_repos

    def get_roi_repos(self) -> ROIRepository:
        """
        Returns an instance of the ROIRepository class.
        :return: Instance of the ROIRepository class.
        """
        return self.roi_repos

    def get_series_repos(self) -> SeriesRepository:
        """
        Returns an instance of the SeriesRepository class.
        :return: Instance of the SeriesRepository class.
        """
        return self.series_repos

    def get_study_repos(self) -> StudyRepository:
        """
        Returns an instance of the StudyRepository class.
        :return: Instance of the StudyRepository class.
        """
        return self.study_repos
