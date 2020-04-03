from typing import Dict, List, Any, Optional

from dal.roi_repository import ROIRepository
from logic.entities.image import Image
from logic.entities.roi import ROI
from logic.roi_selector.roi_selector import ROISelector
from logic.roi_selector.roi_selector_properties import ROISelectorProperties
from logic.entities.rtstruct_series import RtstructSeries


class ROISelectorMockUp(ROISelector):

    get_rois_of_rtstruct_called_with_parameters: List[Dict[Optional[str], Any]] = []
    get_rois_of_rtstruct_return_value: Any = None

    def __init__(self, roi_repos: ROIRepository, roi_selector_properties: ROISelectorProperties) -> None:
        super().__init__(roi_repos, roi_selector_properties)

        self.select_rois_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.select_rois_return_value: Any = None

        self.save_rois_from_rtstruct_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_rois_from_rtstruct_return_value: Any = None

    def select_rois(self, series: RtstructSeries) -> List[ROI]:
        self.select_rois_called_with_parameters.append(
            {
                'series': series
            }
        )
        return self.select_rois_return_value

    def save_rois_from_rtstruct(self, rois: Dict[ROI, int], series: RtstructSeries) -> List[ROI]:
        self.save_rois_from_rtstruct_called_with_parameters.append(
            {
                'rois': rois,
                'series': series
            }
        )
        return self.save_rois_from_rtstruct_return_value

    @staticmethod
    def get_rois_of_rtstruct(rtstruct: Image) -> Dict[ROI, int]:
        ROISelectorMockUp.get_rois_of_rtstruct_called_with_parameters.append(
            {
                'rtstruct': rtstruct
            }
        )
        return ROISelectorMockUp.get_rois_of_rtstruct_return_value

    def get_select_rois_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.select_rois_called_with_parameters

    def set_select_rois_return_value(self, return_value: Any):
        self.select_rois_return_value = return_value

    def get_save_rois_from_rtstruct_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_rois_from_rtstruct_called_with_parameters

    def set_save_rois_from_rtstruct_return_value(self, return_value: Any) -> None:
        self.save_rois_from_rtstruct_return_value = return_value

    def get_get_rois_from_rtstruct_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_rois_of_rtstruct_called_with_parameters

    def set_get_rois_from_rtstruct_return_value(self, return_value = Any) -> None:
        self.get_rois_of_rtstruct_return_value = return_value
