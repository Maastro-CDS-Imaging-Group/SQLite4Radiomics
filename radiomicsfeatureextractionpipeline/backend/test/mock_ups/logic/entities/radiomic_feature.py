from typing import Optional, Any, Dict, List

from logic.entities.radiomic_class import RadiomicClass
from logic.entities.radiomic_feature import RadiomicFeature


class RadiomicFeatureMockUp(RadiomicFeature):

    def __init__(self, radiomic_class: RadiomicClass, name: str, identity: int = -1):
        super().__init__(radiomic_class, name, identity)

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_identity_return_value: Any = None

        self.get_radiomic_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_class_return_value: Any = None

        self.set_radiomic_class_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_radiomic_class_return_value: Any = None

        self.get_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_name_return_value: Any = None

        self.set_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_name_return_value: Any = None

    @property
    def identity(self) -> int:
        self.get_identity_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_identity_return_value

    @identity.setter
    def identity(self, value: int) -> None:
        self.get_identity_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def radiomic_class(self) -> RadiomicClass:
        self.get_radiomic_called_with_parameters.append(
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
    def name(self) -> str:
        self.get_name_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_name_return_value

    @name.setter
    def name(self, value: str) -> None:
        self.set_name_called_with_parameters.append(
            {
                'value': value
            }
        )

    def get_get_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_identity_called_with_parameters

    def set_get_identity_return_value(self, return_value: Any) -> None:
        self.get_identity_return_value = return_value

    def get_set_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_identity_called_with_parameters

    def set_set_identity_return_value(self, return_value: Any) -> None:
        self.set_identity_return_value = return_value

    def get_get_radiomic_class_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_called_with_parameters

    def set_get_radiomic_class_is_called(self, return_value: Any) -> None:
        self.get_radiomic_class_return_value = return_value

    def get_set_radiomic_class_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_radiomic_class_called_with_parameters

    def set_set_radiomic_class_return_value(self, return_value: Any) -> None:
        self.set_radiomic_class_return_value = return_value

    def get_get_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_name_called_with_parameters

    def set_get_name_return_value(self, return_value: Any) -> None:
        self.get_name_return_value: Any = return_value

    def get_set_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_name_called_with_parameters

    def set_set_name_return_value(self, return_value: Any) -> None:
        self.set_name_return_value = return_value
