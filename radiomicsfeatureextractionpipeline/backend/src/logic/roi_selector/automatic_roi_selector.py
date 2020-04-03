from typing import List

from dal.roi_repository import ROIRepository
from logic.entities.roi import ROI
from logic.roi_selector.roi_selector import ROISelector
from logic.roi_selector.roi_selector_properties import ROISelectorProperties
from logic.entities.rtstruct_series import RtstructSeries


class AutomaticROISelector(ROISelector):
    """
    Makes a selection of rois used for feature extraction using the priority of the ROI's
    """

    def __init__(self, roi_repos: ROIRepository, roi_selector_properties: ROISelectorProperties) -> None:
        super().__init__(roi_repos, roi_selector_properties)

    def select_rois(self, series: RtstructSeries) -> List[ROI]:
        """
        Selects the rois of a rtstruct series with the highest priority.
        :param series: The rtstruct series to select the rois from
        :return: returns a list of selected rois.
        """

        # Loads property that tells how much rois it should select.
        number_of_rois_to_select: int = int(self.roi_selector_properties.get_property(
            'number of region of interests to be selected'))
        # Gets a list of prioritised rois from the database and takes the top n rois in the list.
        return self.roi_repos.get_rois_from_series(series)[:number_of_rois_to_select]
