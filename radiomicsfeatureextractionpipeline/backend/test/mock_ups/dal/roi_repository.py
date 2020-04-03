from typing import Optional, List, Dict, Any

from dal.database_connector import DatabaseConnector
from dal.roi_repository import ROIRepository
from dal.series_repository import SeriesRepository
from logic.entities.roi import ROI
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.segmentation import Segmentation
from test.mock_ups.dal.repository import RepositoryMockUp


class ROIRepositoryMockUp(ROIRepository, RepositoryMockUp):

    def __init__(self, database_connector: DatabaseConnector, series_repos: SeriesRepository,
                 query_directory: str) -> None:
        super().__init__(database_connector, series_repos, query_directory)

        self.save_roi_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_roi_return_value: Any = None

        self.get_roi_by_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_roi_by_name_return_value: Any = None

        self.get_roi_by_id_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_roi_by_id_return_value: Any = None

        self.get_rois_of_priority_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_rois_of_priority_return_value: Any = None

        self.update_roi_priority_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.update_roi_priority_return_value: Any = None

        self.save_segmentation_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_segmentation_return_value: Any = None

        self.get_dicom_segmentation_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_dicom_segmentation_return_value: Any = None

        self.get_rois_from_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_rois_from_series_return_value: Any = None

        self.series_roi_exist_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.series_roi_exist_return_value: Any = None

        self.update_dicom_seg_file_path_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.update_dicom_seg_file_path_return_value: Any = None

    def save_roi(self, roi: ROI) -> None:
        self.save_roi_called_with_parameters.append(
            {
                'roi': roi
            }
        )
        return self.save_roi_return_value

    def get_roi_by_name(self, roi_name: str) -> Optional[ROI]:
        self.get_roi_by_name_called_with_parameters.append(
            {
                'roi_name': roi_name
            }
        )
        return self.get_roi_by_name_return_value

    def get_roi_by_id(self, roi_id: int) -> Optional[ROI]:
        self.get_roi_by_id_called_with_parameters.append(
            {
                'roi_id': roi_id
            }
        )
        return self.get_roi_by_id_return_value

    def get_rois_of_priority(self, priority: int) -> List[ROI]:
        self.get_rois_of_priority_called_with_parameters.append(
            {
                'priority': priority
            }
        )
        return self.get_rois_of_priority_return_value

    def update_roi_priority(self, roi: ROI) -> None:
        self.update_roi_priority_called_with_parameters.append(
            {
                'roi': roi
            }
        )
        return self.update_roi_priority_return_value

    def save_segmentation(self, dicom_segmentation: Segmentation = None) -> None:
        self.save_segmentation_called_with_parameters.append(
            {
                'dicom_segmentation': dicom_segmentation
            }
        )
        return self.save_segmentation_return_value

    def get_dicom_segmentation(self, series: RtstructSeries, roi: ROI) -> Segmentation:
        self.get_dicom_segmentation_called_with_parameters.append(
            {
                'series': series,
                'roi': roi
            }
        )
        return self.get_dicom_segmentation_return_value

    def get_rois_from_series(self, series: RtstructSeries) -> List[ROI]:
        self.get_rois_from_series_called_with_parameters.append(
            {
                'series': series
            }
        )
        return self.get_rois_from_series_return_value

    def segmentation_exists(self, segmentation: Segmentation) -> bool:
        self.series_roi_exist_called_with_parameters.append(
            {
                'segmentation': segmentation
            }
        )
        return self.series_roi_exist_return_value

    def update_dicom_seg_file_path(self, segmentation: Segmentation) -> None:
        self.update_dicom_seg_file_path_called_with_parameters.append(
            {
                'segmentation': segmentation
            }
        )
        return self.update_dicom_seg_file_path_return_value

    def get_save_roi_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_roi_called_with_parameters

    def set_save_roi_return_value(self, return_value: Any) -> None:
        self.save_roi_return_value = return_value

    def get_get_roi_by_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_roi_by_name_called_with_parameters

    def set_get_roi_by_name_return_value(self, return_value: Any) -> None:
        self.get_roi_by_name_return_value: Optional[ROI] = return_value

    def get_get_roi_by_id_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_roi_by_id_called_with_parameters

    def set_get_roi_by_id_return_value(self, return_value: Any) -> None:
        self.get_roi_by_id_return_value = return_value

    def get_get_rois_of_priority_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_rois_of_priority_called_with_parameters

    def set_get_rois_of_priority_return_value(self, return_value: Any) -> None:
        self.get_rois_of_priority_return_value = return_value

    def get_update_roi_priority_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.update_roi_priority_called_with_parameters

    def set_update_roi_priority_return_value(self, return_value: Any) -> None:
        self.update_roi_priority_return_value = return_value

    def get_save_segmentation_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_segmentation_called_with_parameters

    def get_save_segmentation_return_value(self, return_value: Any) -> None:
        self.save_segmentation_return_value = return_value

    def get_get_dicom_segmentation_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_dicom_segmentation_called_with_parameters

    def set_get_dicom_segmentation_return_value(self, return_value: Segmentation) -> None:
        self.get_dicom_segmentation_return_value: Segmentation = return_value

    def get_get_rois_from_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_rois_from_series_called_with_parameters

    def set_get_rois_from_series_return_value(self, return_value: Any) -> None:
        self.get_rois_from_series_return_value = return_value

    def get_series_roi_exist_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.series_roi_exist_called_with_parameters

    def set_series_roi_exist_return_value(self, return_value: Any) -> None:
        self.series_roi_exist_return_value = return_value

    def get_update_dicom_seg_file_path_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.update_dicom_seg_file_path_called_with_parameters

    def set_update_dicom_seg_file_path_return_value(self, return_value):
        self.update_dicom_seg_file_path_return_value = return_value
