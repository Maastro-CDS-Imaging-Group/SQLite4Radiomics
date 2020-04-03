from typing import Optional, Any, Dict, List

from logic.entities.radiomic_class import RadiomicClass
from logic.entities.radiomic_feature import RadiomicFeature
from logic.entities.radiomic_feature_value import RadiomicFeatureValue
from logic.entities.radiomic_filter import RadiomicFilter
from logic.entities.roi import ROI


class RadiomicFeatureValueMockUp(RadiomicFeatureValue):

    def __init__(self, roi: ROI, radiomic_filter: RadiomicFilter, radiomic_class: RadiomicClass,
                 feature: RadiomicFeature, value: str):
        super().__init__(roi, radiomic_filter, radiomic_class, feature, value)

        self.get_roi_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_roi_return_value: Any = None

        self.set_roi_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_roi_return_value: Any = None

        self.get_radiomic_filter_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_filter_return_value: Any = None

        self.set_radiomic_filter_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_radiomic_filter_return_value: Any = None

        self.get_radiomic_class_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_class_return_value: Any = None

        self.set_radiomic_class_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_radiomic_class_return_value: Any = None

        self.get_feature_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_feature_return_value: Any = None

        self.set_feature_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_feature_return_value: Any = None

        self.get_value_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_value_return_value: Any = None

        self.set_value_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_value_return_value: Any = None

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
    def radiomic_filter(self) -> RadiomicFilter:
        self.set_roi_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_radiomic_filter_return_value

    @radiomic_filter.setter
    def radiomic_filter(self, value: RadiomicFilter) -> None:
        self.set_radiomic_filter_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def radiomic_class(self) -> RadiomicClass:
        self.get_radiomic_class_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_radiomic_class_return_value

    @radiomic_class.setter
    def radiomic_class(self, value: RadiomicClass) -> None:
        self.set_radiomic_class_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def feature(self) -> RadiomicFeature:
        self.get_feature_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_feature_return_value

    @feature.setter
    def feature(self, value: RadiomicFeature) -> None:
        self.set_feature_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def value(self) -> str:
        self.get_value_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_value_return_value

    @value.setter
    def value(self, value: str) -> None:
        self.set_value_called_with_parameters.append(
            {
                'value': value
            }
        )

    def get_get_roi_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_roi_called_with_parameters

    def set_get_roi_return_value(self, return_value: Any) -> None:
        self.get_roi_return_value = return_value

    def get_set_roi_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_roi_called_with_parameters

    def set_set_roi_return_value(self, return_value: Any) -> None:
        self.set_roi_return_value = return_value

    def get_get_radiomic_filter_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_filter_called_with_parameters

    def set_get_radiomic_filter_return_value(self, return_value: Any) -> None:
        self.get_radiomic_filter_return_value = return_value

    def get_set_radiomic_filter_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_radiomic_filter_called_with_parameters

    def set_set_radiomic_filter_return_value(self, return_value: Any) -> None:
        self.set_radiomic_filter_return_value = return_value

    def get_get_radiomic_class_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_class_called_with_parameters

    def set_get_radiomic_class_return_value(self, return_value: Any) -> None:
        self.get_radiomic_class_return_value = return_value

    def get_set_radiomic_class_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_radiomic_class_called_with_parameters

    def set_set_radiomic_class_return_value(self, return_value) -> None:
        self.set_radiomic_class_return_value = return_value

    def get_get_feature_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_feature_called_with_parameters

    def set_get_feature_return_value(self, return_value: Any) -> None:
        self.get_feature_return_value = return_value

    def get_set_feature_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_feature_called_with_parameters

    def set_set_feature_return_value(self, return_value: Any) -> None:
        self.set_feature_return_value = return_value

    def get_get_value_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_value_called_with_parameters

    def set_get_value_return_value(self, return_value: Any) -> None:
        self.get_value_return_value = return_value

    def get_set_value_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_value_called_with_parameters

    def set_set_value_return_value(self, return_value: Any) -> None:
        self.set_value_return_value = return_value
