from typing import Optional, Any, Dict, List

from logic.entities.roi import ROI
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.segmentation import Segmentation


class SegmentationMockUp(Segmentation):

    def __init__(self, roi: ROI, series: RtstructSeries, number: int, file_path: str) -> None:
        super().__init__(roi, series, number, file_path)

        self.get_roi_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_roi_return_value: Any = None

        self.set_roi_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_roi_return_value: Any = None

        self.get_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_series_return_value: Any = None

        self.set_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_series_return_value: Any = None

        self.get_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_number_return_value: Any = None

        self.set_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_number_return_value: Any = None

        self.get_file_path_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_file_path_return_value: Any = None

        self.set_file_path_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_file_path_return_value: Any = None

    @property
    def roi(self) -> ROI:
        self.get_roi_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_roi_return_value

    @roi.setter
    def roi(self, value: ROI) -> None:
        self.set_roi_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def series(self) -> RtstructSeries:
        self.get_series_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_series_return_value

    @series.setter
    def series(self, value: RtstructSeries) -> None:
        self.set_series_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def number(self) -> int:
        self.get_number_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_number_return_value

    @number.setter
    def number(self, value: int) -> None:
        self.set_number_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def file_path(self) -> str:
        self.get_file_path_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_file_path_return_value

    @file_path.setter
    def file_path(self, value: str) -> None:
        self.set_file_path_called_with_parameters.append(
            {
                'value': value
            }
        )

    def get_get_roi_called_with_parameters_file(self) -> List[Dict[Optional[str], Any]]:
        return self.get_roi_called_with_parameters

    def set_get_roi_return_value(self, return_value: Any) -> None:
        self.get_roi_return_value = return_value

    def get_set_roi_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_roi_called_with_parameters

    def set_set_roi_return_value(self, return_value: Any) -> None:
        self.set_roi_return_value = return_value

    def get_get_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_series_called_with_parameters

    def set_get_series_return_value(self, return_value: Any) -> None:
        self.get_series_return_value = return_value

    def get_set_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_series_called_with_parameters

    def set_set_series_return_value(self, return_value: Any) -> None:
        self.set_series_return_value = return_value

    def get_get_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_number_called_with_parameters

    def set_get_number_return_value(self, return_value: Any) -> None:
        self.get_number_return_value = return_value

    def get_set_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_number_called_with_parameters

    def set_set_number_return_value(self, return_value: Any) -> None:
        self.set_number_return_value = return_value

    def get_get_file_path_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_file_path_called_with_parameters

    def set_get_file_path_return_value(self, return_value: Any) -> None:
        self.get_file_path_return_value = return_value

    def get_set_file_path_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_file_path_called_with_parameters

    def set_set_file_path_called_with_return_value(self, return_value: Any) -> None:
        self.set_file_path_return_value = return_value
