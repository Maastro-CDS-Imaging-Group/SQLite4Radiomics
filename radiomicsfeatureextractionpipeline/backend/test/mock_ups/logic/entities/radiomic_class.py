from typing import Optional, Any, Dict, List

from logic.entities.radiomic_class import RadiomicClass


class RadiomicClassMockUp(RadiomicClass):

    def __init__(self, name: str, identity: int = -1, parent_class: RadiomicClass = None):
        super().__init__(name, identity, parent_class)

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_identity_return_value: Any = None

        self.get_parent_class_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_parent_class_return_value: Any = None

        self.set_parent_class_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_parent_class_return_value: Any = None

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
        self.set_identity_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def parent_class(self) -> RadiomicClass:
        self.get_parent_class_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_parent_class_return_type

    @parent_class.setter
    def parent_class(self, value: RadiomicClass) -> None:
        self.set_parent_class_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def name(self) -> str:
        self.set_parent_class_called_with_parameters.append(
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

    def get_get_identity_is_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_identity_called_with_parameters

    def set_get_identity_return_value(self, return_value: Any) -> None:
        self.get_identity_return_value = return_value

    def get_set_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_identity_called_with_parameters

    def set_set_identity_return_value(self, return_value: Any) -> None:
        self.set_identity_return_value = return_value

    def get_get_parent_class_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_parent_class_called_with_parameters

    def set_get_parent_class_return_value(self, return_value: Any) -> None:
        self.get_parent_class_return_type = return_value

    def get_set_parent_class_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_parent_class_called_with_parameters

    def set_set_parent_class_return_value(self, return_value: Any) -> None:
        self.set_parent_class_return_value = return_value

    def get_get_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_name_called_with_parameters

    def set_get_name_return_value(self, return_value) -> None:
        self.get_name_return_value = return_value

    def get_set_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_name_called_with_parameters

    def set_set_name_return_value(self, return_value: Any) -> None:
        self.set_name_return_value = return_value