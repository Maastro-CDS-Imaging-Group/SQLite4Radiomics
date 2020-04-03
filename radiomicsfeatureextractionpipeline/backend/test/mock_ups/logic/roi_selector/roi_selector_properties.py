from typing import Optional, Dict, Any, List

from logic.roi_selector.roi_selector_properties import ROISelectorProperties


class ROISelectorPropertiesMockUp(ROISelectorProperties):

    def __init__(self, properties: Optional[Dict[str, str]] = None) -> None:
        super().__init__(properties)

        self.set_property_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_property_return_value: Any = None

        self.get_property_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_property_return_value: Any = None

        self.remove_property_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.remove_property_return_value: Any = None

    def set_property(self, name: str, value: str) -> None:
        self.set_property_called_with_parameters.append(
            {
                'name': name,
                'value': value
            }
        )
        return self.set_property_return_value

    def get_property(self, name: str) -> str:
        self.get_property_called_with_parameters.append(
            {
                'name': name
            }
        )
        return self.get_property_return_value

    def remove_property(self, name: str) -> None:
        self.remove_property_called_with_parameters.append(
            {
                'name': name
            }
        )
        return self.remove_property_return_value

    def get_set_property_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_property_called_with_parameters

    def set_set_property_return_value(self, return_value: Any) -> None:
        self.set_property_return_value = return_value

    def get_get_property_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_property_called_with_parameters

    def set_get_property_return_value(self, return_value: Any) -> None:
        self.get_property_return_value = return_value

    def get_remove_property_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.remove_property_called_with_parameters

    def set_remove_property_return_value(self, return_value: Any) -> None:
        self.remove_property_return_value = return_value
