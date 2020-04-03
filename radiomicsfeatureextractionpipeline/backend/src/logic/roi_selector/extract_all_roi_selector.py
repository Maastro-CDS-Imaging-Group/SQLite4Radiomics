from typing import List

from dal.roi_repository import ROIRepository
from logic.entities.roi import ROI
from logic.roi_selector.roi_selector import ROISelector
from logic.roi_selector.roi_selector_properties import ROISelectorProperties
from logic.entities.rtstruct_series import RtstructSeries


class ExtractAllROISelector(ROISelector):
    
    def __init__(self, roi_repos: ROIRepository,
                 roi_selector_properties: ROISelectorProperties) -> None:
        ROISelector.__init__(self, roi_repos, roi_selector_properties)
    
    def select_rois(self, series: RtstructSeries) -> List[ROI]:
        return self.roi_repos.get_rois_from_series(series)
