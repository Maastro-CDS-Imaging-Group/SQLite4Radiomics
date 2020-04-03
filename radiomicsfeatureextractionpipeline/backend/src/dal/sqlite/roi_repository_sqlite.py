"""
This module handles the loading and saving of images.
It inherits from the ROIRepository class.
"""

from typing import List, Optional, Any, Dict, Callable

import pandas as pd

from dal.database_connector import DatabaseConnector
from dal.database_error import DatabaseError
from dal.roi_repository import ROIRepository
from dal.series_repository import SeriesRepository
from logic.entities.roi import ROI
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.segmentation import Segmentation


class ROIRepositorySqlite(ROIRepository):
    """
    Handles all transaction to the database regarding ROI and Segmentation objects
    """

    def __init__(self, database_connector: DatabaseConnector, series_repository: SeriesRepository,
                 query_directory: str) -> None:
        """
        Constructor for the ROIRepositorySqlite
        :param database_connector: The database connector that will communicate with the database.
        :param series_repository: The repository that handles all the loading and saving of series.
        :param query_directory: The directory of the SQL-files
        """
        super().__init__(database_connector, series_repository, query_directory)

    def save_roi(self, roi: ROI) -> None:
        """
        Saves the ROI to the database.
        :param roi: The ROI to save.
        :return: The updated ROI with identity.
        """

        sql_file_path: str = r"{0}\roi\save_roi.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': roi.name, 'priority': roi.priority}
        roi_exist_checker: Callable[[ROI], bool] = self.roi_exists
        roi_to_save: ROI = roi

        self.save_object(sql_file_path, sql_parameters, roi_exist_checker, roi_to_save)

    def roi_exists(self, roi: ROI) -> bool:
        """
        Checks whether a ROI exists in the database
        :param roi: The ROI to check.
        :return: Returns True if ROI is int he database. Returns False if it isn't.
        """

        sql_file_path: str = r"{0}\roi\roi_exists.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': roi.name}

        return self.check_if_object_exist_in_database(sql_file_path, sql_parameters)

    def get_roi_by_name(self, roi_name: str) -> Optional[ROI]:
        """
        Gets the ROI object corresponding to the name.
        :param roi_name: The name of the ROI.
        :return: The ROI object that corresponds to the given name.
        """

        sql_file_path: str = r"{0}\roi\get_roi_by_name.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'name': roi_name}
        record_to_roi_converter: Callable[[pd.Series], ROI] = self.__query_result_to_roi

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_roi_converter)

    def get_roi_by_id(self, roi_id: int) -> Optional[ROI]:
        """
        Gets the ROI object corresponding to it's identifier.
        :param roi_id: The identifier of the ROI.
        :return: The ROI object that corresponds to the identifier.
        """

        sql_file_path: str = r"{0}\roi\get_roi_by_id.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'id': roi_id}
        record_to_roi_converter: Callable[[pd.Series], ROI] = self.__query_result_to_roi

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_roi_converter)

    def get_rois_of_priority(self, priority: int) -> List[ROI]:
        """
        Gets a list of all rois with a specific priority.
        :param priority: The priority of to filter the ROI's for,
        :return: A list of all ROI's that match the priority requirement.
        """

        sql_file_path: str = r"{0}\roi\get_rois_of_priority.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'priority': priority}
        record_to_roi_converter: Callable[[pd.Series], ROI] = self.__query_result_to_roi

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_roi_converter)

    def update_roi_priority(self, roi: ROI) -> None:
        """
        Saves the new ROI to the database.
        :param roi: The ROI with the changed priority.
        :return: The method doesn't return anything.
        """

        sql_file_path: str = r"{0}\roi\update_roi_priority.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'priority': roi.priority, 'name': roi.name}

        self.execute_non_query(sql_file_path, sql_parameters)

    def save_segmentation(self, dicom_segmentation: Segmentation = None) -> None:
        """
        Saves the dicom segmentation to the database.
        :param dicom_segmentation: The dicom segmentation that needs to be saved.
        :return: The method doesn't return anything.
        """

        sql_file_path: str = r"{0}\roi_series\save_series_roi.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'roi_id': int(dicom_segmentation.roi.identity),
                                          'series_instance': dicom_segmentation.series.identity,
                                          'number': int(dicom_segmentation.number),
                                          'dicom_seg_file': dicom_segmentation.file_path}
        segmentation_exist_checker: Callable[[Segmentation], bool] = self.segmentation_exists
        segmentation_to_save: Segmentation = dicom_segmentation

        self.save_object(sql_file_path, sql_parameters, segmentation_exist_checker, segmentation_to_save)

    def get_dicom_segmentation(self, series: RtstructSeries, roi: ROI) -> Optional[Segmentation]:
        """
        Gets the Segmentation corresponding to the given RTSTRUCT-series and ROI.
        :param series: The RTSTRUCT-series to get the Segmentation from.
        :param roi: The ROI to get the Segmentation from.
        :return: The Segmentation object that corresponds to the RTSTRUCT-series and the ROI.
        """

        sql_file_path: str = r"{0}\roi_series\get_dicom_segmentation.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'roi_id': roi.identity, 'series_id': series.identity}
        record_to_segmentation_converter: Callable[[pd.Series], Segmentation] = self.__query_result_to_segmentation

        return self.get_single_object_by_constrained(sql_file_path, sql_parameters, record_to_segmentation_converter)

    def get_rois_from_series(self, series: RtstructSeries) -> List[ROI]:
        """
        Gets a list form all ROI's of the given RTSTRUCT-series.
        :param series: The RTSTRUCT-series to get the ROI's from.
        :return: A list of ROI's that belongs to the RTSTRUCT-series.
        """

        sql_file_path: str = r"{0}\roi_series\get_rois_from_series.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'series_id': series.identity}
        record_to_roi_converter: Callable[[pd.Series], ROI] = self.__query_result_to_roi

        return self.get_all_by_constrained(sql_file_path, sql_parameters, record_to_roi_converter)

    def segmentation_exists(self, segmentation: Segmentation) -> bool:
        """
        Checks whether the series-roi is already stored in the database.
        :param segmentation: The segmentation to check.
        :return: Returns whether the series-roi exists.
        """

        sql_file_path = r"{0}\roi_series\series_roi_exist.sql".format(self.query_file_directory)
        sql_parameters = {'roi_id': int(segmentation.roi.identity), 'series_id': segmentation.series.identity}

        return self.check_if_object_exist_in_database(sql_file_path, sql_parameters)

    def update_dicom_seg_file_path(self, segmentation: Segmentation) -> None:
        """
        Updates the file path of the dicom-segmentation file.
        :param segmentation: The segmentation to update.
        :return: The method doesn't return anything.
        """

        sql_file_path: str = r"{0}\roi_series\update_dicom_seg_file_path.sql".format(self.query_file_directory)
        sql_parameters: Dict[str, Any] = {'dicom_seg_file': segmentation.file_path,
                                          'roi_id': segmentation.roi.identity,
                                          'series_id': segmentation.series.identity}

        self.execute_non_query(sql_file_path, sql_parameters)

    @staticmethod
    def __query_result_to_roi(record: pd.Series) -> ROI:
        """
        Converts record in DICOMROI table to ROI object.
        :param record: One record of the table returned by the database.
        :return: ROI object created with the data in the record.
        """

        roi_id: int = record["RoiId"]
        roi_name: str = record["Name"]
        roi_priority: int = record['Priority']

        # Create ROI object from table row.
        return ROI(roi_name, roi_id, roi_priority)

    def __query_result_to_segmentation(self, record: pd.Series) -> Segmentation:
        """
        Converts record in DICOMSeriesROI table to Segmentation object.
        :param record: One record of the table returned by the database.
        :return: Segmentation object created with the data in the record.
        """
        roi_id: int = record["RoiId"]
        series_instance: str = record["SeriesInst"]
        number: int = record["Number"]
        dicom_seg_file: str = record["DicomSegFile"]

        # Gets the roi object corresponding to the identification number in the database.
        roi: ROI = self.get_roi_by_id(roi_id)

        # Gets the Series object corresponding to the identification number in the database.
        series: pd.Series = self.series_repos.get_series_from_id(series_instance)

        # Checks whether the returned series is an RTSTRUCT-series.
        if not isinstance(series, RtstructSeries):
            raise DatabaseError("The program failed to load a Segmentation from the database."
                                " A RTSTRUCT-series expected but not returned.")

        series: RtstructSeries
        # Create Segmentation object from table row.
        return Segmentation(roi, series, number, dicom_seg_file)
