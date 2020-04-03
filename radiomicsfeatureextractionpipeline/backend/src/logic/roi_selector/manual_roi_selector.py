from typing import List

from dal.roi_repository import ROIRepository
from logic.entities.roi import ROI
from logic.roi_selector.roi_selector import ROISelector
from logic.roi_selector.roi_selector_properties import ROISelectorProperties
from logic.entities.rtstruct_series import RtstructSeries


class ManualROISelector(ROISelector):

    def __init__(self, roi_repos: ROIRepository, roi_selector_properties: ROISelectorProperties) -> None:
        ROISelector.__init__(self, roi_repos, roi_selector_properties)
    
    def select_rois(self, series: RtstructSeries) -> List[ROI]:
        available_rois: List[ROI] = self.roi_repos.get_rois_from_series(series)
        target_rois: List[str] = self.roi_selector_properties.get_property('manual selection').split(', ')
        return [roi for roi in available_rois if roi.name == target_rois]
