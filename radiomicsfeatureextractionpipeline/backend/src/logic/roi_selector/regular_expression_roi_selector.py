import re
from typing import List, Union, Pattern

from numpy import byte

from dal.roi_repository import ROIRepository
from logic.entities.roi import ROI
from logic.roi_selector.roi_selector import ROISelector
from logic.roi_selector.roi_selector_properties import ROISelectorProperties
from logic.entities.rtstruct_series import RtstructSeries


class RegularExpressionROISelector(ROISelector):

    def __init__(self, roi_repos: ROIRepository, roi_selector_properties: ROISelectorProperties):
        super().__init__(roi_repos, roi_selector_properties)

    def select_rois(self, series: RtstructSeries) -> List[ROI]:
        regex: Union[Pattern[Union[str, byte]], Pattern] = re.compile(
            self.roi_selector_properties.get_property("regular expression"))
        series_rois: List[ROI] = self.roi_repos.get_rois_from_series(series)
        return [roi for roi in series_rois if regex.fullmatch(roi.name.lower())]
