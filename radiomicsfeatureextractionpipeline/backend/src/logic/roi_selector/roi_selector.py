from abc import ABC, abstractmethod
from typing import List, Dict

import pydicom
import pydicom as dicom

from dal.roi_repository import ROIRepository
from logic.entities.image import Image
from logic.entities.roi import ROI
from logic.entities.segmentation import Segmentation
from logic.roi_selector.roi_selector_properties import ROISelectorProperties
from logic.entities.rtstruct_series import RtstructSeries


class ROISelector(ABC):
    """
    Abstract base class for implementation of the strategy pattern.
    Used for selection region of Interests
    """

    def __init__(self, roi_repos: ROIRepository, roi_selector_properties: ROISelectorProperties) -> None:
        """
        Constructor RegionOfInterestSelector class
        :param region_of_interest_selector_properties: properties that can be used during roi selection.
        """
        self.roi_repos: ROIRepository = roi_repos
        self.roi_selector_properties: ROISelectorProperties = roi_selector_properties

    @abstractmethod
    def select_rois(self, series: RtstructSeries) -> List[ROI]:
        """
        Selects the Region Of Interests to be used for Radiomic feature extraction.
        :param series: RTSTRUCT series which needs to be analysed
        :return: list of selected Region Of Interests
        """
        pass

    def save_rois_from_rtstruct(self, rois: Dict[ROI, int], series: RtstructSeries) -> List[ROI]:
        """
        Saves all rois found in RTSTRUCT file.
        :param rois: List of Region of interests that needs to be saved
        :param series: The RTSTRUCT series that the Region of Interests come from.
        :return: Method has no return value.
        """
        new_rois: List[ROI] = []

        roi: ROI
        number: int
        for roi, number in rois.items():
            self.roi_repos.save_roi(roi)
            new_roi: ROI = self.roi_repos.get_roi_by_name(roi.name)
            segmentation: Segmentation = Segmentation(new_roi, series, number, '')
            self.roi_repos.save_segmentation(segmentation)
            new_rois.append(new_roi)
        return new_rois

    @staticmethod
    def get_rois_of_rtstruct(rtstruct: Image) -> Dict[ROI, int]:
        """
        Reads all Region of interests available in RTSTRUCT file.
        :param rtstruct: RTSTRUCT file to read.
        :return: returns a list of all rois found in the RTSTRUCT file
        """

        rois: Dict[ROI, int] = {}

        roi_data: pydicom.FileDataset
        for roi_data in rtstruct.content.StructureSetROISequence:
            rois[ROI(roi_data.ROIName)]: Dict[ROI, int] = roi_data.ROINumber
        return rois
