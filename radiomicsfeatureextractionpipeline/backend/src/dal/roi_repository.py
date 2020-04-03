"""
THis module is used as a template for all ROIRepositories.
All ImageRepositories in the data access layer should inherit from this class.
Inherits the Repository class.
"""
from abc import abstractmethod
from typing import List, Optional

from dal.database_connector import DatabaseConnector
from dal.repository import Repository
from dal.series_repository import SeriesRepository
from logic.entities.roi import ROI
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.segmentation import Segmentation


class ROIRepository(Repository):
    """
    This class is a template for te repository that handles all the loading and saving of ROI's.
    """

    def __init__(self, database_connector: DatabaseConnector, series_repos: SeriesRepository,
                 queries_file_directory: str) -> None:
        """
        Constructor for the ROIRepository class.
        :param database_connector: The database connector that will communicate with the database.
        :param series_repos: The repository that handles all the loading and saving of series.
        :param queries_file_directory: The directory of the SQL-files.
        """
        super().__init__(database_connector, queries_file_directory)
        self.series_repos: SeriesRepository = series_repos

    @abstractmethod
    def save_roi(self, roi: ROI) -> ROI:
        """
        Saves the ROI to the database.
        :param roi: The ROI to save.
        :return: The updated ROI with identity.
        """
        pass

    @abstractmethod
    def roi_exists(self, roi: ROI) -> bool:
        """
        Checks whether a ROI exists in the database
        :param roi: The ROI to check.
        :return: Returns True if ROI is int he database. Returns False if it isn't.
        """
        pass

    @abstractmethod
    def get_roi_by_name(self, roi_name: str) -> Optional[ROI]:
        """
        Gets the ROI object corresponding to it's name.
        :param roi_name: The name of the ROI.
        :return: The ROI object that corresponds to the name.
        """
        pass

    @abstractmethod
    def get_roi_by_id(self, roi_id: int) -> Optional[ROI]:
        """
        Gets the ROI object corresponding to it's identifier.
        :param roi_id: The identifier of the ROI.
        :return: The ROI object that corresponds to the identifier.
        """
        pass

    @abstractmethod
    def get_rois_of_priority(self, priority: int) -> List[ROI]:
        """
        Gets a list of all rois with a specific priority.
        :param priority: The priority of to filter the ROI's for,
        :return: A list of all ROI's that match the priority requirement.
        """
        pass

    @abstractmethod
    def get_rois_from_series(self, series: RtstructSeries) -> List[ROI]:
        """
        Gets a list form all ROI's of the given RTSTRUCT-series.
        :param series: The RTSTRUCT-series to get the ROI's from.
        :return: A list of ROI's that belongs to the RTSTRUCT-series.
        """
        pass

    @abstractmethod
    def get_dicom_segmentation(self, series: RtstructSeries, roi: ROI) -> Segmentation:
        """
        Gets the Segmentation corresponding to the given RTSTRUCT-series and ROI.
        :param series: The RTSTRUCT-series to get the Segmentation from.
        :param roi: The ROI to get the Segmentation from.
        :return: The Segmentation object that corresponds to the RTSTRUCT-series and the ROI.
        """
        pass

    @abstractmethod
    def save_segmentation(self, dicom_segmentation: Segmentation = None) -> None:
        """
        Saves the dicom segmentation to the database.
        :param dicom_segmentation: The dicom segmentation that needs to be saved.
        :return: The method doesn't return anything.
        """
        pass

    @abstractmethod
    def update_roi_priority(self, roi: ROI) -> None:
        """
        Saves the new ROI to the database.
        :param roi: The ROI with the changed priority.
        :return: The method doesn't return anything.
        """
        pass

    @abstractmethod
    def segmentation_exists(self, segmentation: Segmentation) -> bool:
        """
        Checks whether the series-roi is already stored in the database.
        :param segmentation: The segmentation to check
        :return: Returns whether the series-roi exists.
        """
        pass

    @abstractmethod
    def update_dicom_seg_file_path(self, segmentation: Segmentation) -> None:
        """
        Updates the file path of the dicom-segmentation file.
        :param series: The series belonging to the dicom-segmentation-file.
        :param roi: The ROI belonging to the dicom-segmentation-file.
        :param dicom_seg_file_path: The updated path to the dicom-segmentation-file.
        :return: The method doesn't return anything.
        """
        pass
