from typing import Optional, Any, Dict, List

from logic.entities.radiomic_filter import RadiomicFilter


class RadiomicFilterMockUp(RadiomicFilter):

    def __init__(self, name: str, identity: int = -1) -> None:
        super().__init__(name, identity)

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_identity_return_value: Any = None

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

    def set_set_identity_return_value(self, return_value: str) -> None:
        self.set_identity_return_value = return_value

    def get_get_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_name_called_with_parameters

    def set_get_name_return_value(self, return_value: Any) -> None:
        self.get_name_return_value = return_value

    def get_set_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_name_called_with_parameters

    def set_set_name_return_value(self, return_value: Any) -> None:
        self.set_name_return_value = return_value
