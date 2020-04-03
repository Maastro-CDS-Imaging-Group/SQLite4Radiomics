from typing import AbstractSet, Tuple, Any, Dict, Optional, List

from configuration_service.config_file_reader import ConfigFileReader


class ConfigFileReaderMockUp(ConfigFileReader):

    def __init__(self, config_file_path: str) -> None:
        super().__init__(config_file_path)

        self.read_property_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.read_property_return_value: Any = None

        self.save_property_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_property_return_value: Any = None

        self.add_section_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.add_section_return_value: Any = None

        self.get_all_properties_from_section_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_properties_from_section_return_value: Any = None

        self.section_exists_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.section_exists_return_value: Any = None

        self.option_exists_is_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.option_exists_return_value: Any = None

    def read_property(self, section_name: str, property_name: str) -> str:
        self.read_property_called_with_parameters.append(
            {
                'section_name': section_name,
                'property_name': property_name
            }
        )
        print(self.read_property_called_with_parameters)
        return self.read_property_return_value

    def save_property(self, section_name: str, property_name: str, property_value: str) -> None:
        self.save_property_called_with_parameters.append(
            {
                'section_name': section_name,
                'property_name': property_name,
                'property_value': property_value
            }
        )
        return self.save_property_return_value

    def add_section(self, section_name: str) -> None:
        self.add_section_called_with_parameters.append(
            {
                'section_name': section_name
            }
        )
        return self.add_section_return_value

    def get_all_properties_from_section(self, section_name: str) -> AbstractSet[Tuple[Any, Any]]:
        self.get_all_properties_from_section_called_with_parameters.append(
            {
                'section_name': section_name
            }
        )
        return self.get_all_properties_from_section_return_value

    def section_exists(self, section_name: str) -> bool:
        self.section_exists_called_with_parameters.append(
            {
                'section_name': section_name
            }
        )
        return self.section_exists_return_value

    def option_exists(self, section_name: str, option_name: str) -> bool:
        self.option_exists_is_called_with_parameters.append(
            {
                'section_name' : section_name,
                'option_name': option_name
            }
        )
        return self.section_exists_return_value

    def get_read_property_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.read_property_called_with_parameters

    def set_read_property_return_value(self, return_value: Any) -> None:
        self.read_property_return_value = return_value

    def get_save_property_is_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_property_called_with_parameters

    def set_save_property_return_value(self, return_value: Any) -> None:
        self.save_property_return_value = return_value

    def get_add_section_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.add_section_called_with_parameters

    def set_add_section_called_with_parameters(self, return_value: Any) -> None:
        self.add_section_return_value = return_value

    def get_get_properties_from_section_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_properties_from_section_called_with_parameters

    def set_get_properties_from_section_return_value(self, return_value: Any) -> None:
        self.get_all_properties_from_section_return_value = return_value

    def get_section_exists_called_with_parameter(self) -> List[Dict[Optional[str], Any]]:
        return self.section_exists_called_with_parameters

    def set_section_exists_return_value(self, return_value: Any) -> None:
        self.section_exists_return_value = return_value

    def get_option_exists_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.option_exists_is_called_with_parameters

    def set_option_exists_return_value(self, return_value: Any) -> None:
        self.option_exists_return_value = return_value
