from typing import Optional, Dict, List, Any

from configuration_service.config_file_reader import ConfigFileReader
from configuration_service.configuration_service import ConfigurationService


class ConfigurationServiceMockUp(ConfigurationService):

    def __init__(self, config_file_reader: ConfigFileReader) -> None:
        super().__init__(config_file_reader)

        self.save_database_settings_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_database_settings_return_value: Any = None

        self.load_database_settings_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.load_database_settings_return_value: Any = None

        self.save_data_directory_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_data_directory_return_value: Any = None

        self.load_data_directory_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.load_data_directory_return_value: Any = None

        self.load_region_of_interest_selector_properties_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.load_region_of_interest_selector_properties_return_value: Any = None

        self.load_strategy_selection_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.load_strategy_selection_return_value: Any = None

        self.load_strategy_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.load_strategy_return_value: Any = None

        self.load_radiomics_params_file_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.load_radiomics_params_file_return_value: Any = None

        self.load_database_type_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.load_database_type_return_value: Any = None

    def save_database_settings(self, connection_string: str) -> None:
        self.save_database_settings_called_with_parameters.append(
            {
                'connection_string': connection_string
            }
        )

    def load_database_settings(self) -> Optional[str]:
        self.load_database_settings_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.load_database_settings_return_value

    def save_data_directory(self, data_directory: str) -> None:
        self.save_data_directory_called_with_parameters.append(
            {
                'data_directory': data_directory
            }
        )
        return self.save_data_directory_return_value

    def load_data_directory(self) -> str:
        self.load_data_directory_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.load_data_directory_return_value

    def load_roi_selector_properties(self) -> Dict[str, str]:
        self.load_region_of_interest_selector_properties_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.load_region_of_interest_selector_properties_return_value

    def load_strategy_selection(self, strategy_type: str) -> str:
        self.load_strategy_selection_called_with_parameters.append(
            {
                'strategy_type': strategy_type
            }
        )
        return self.load_strategy_selection_return_value

    def load_strategy(self, strategy_type: str, selected_strategy: str) -> str:
        self.load_strategy_called_with_parameters.append(
            {
                'strategy_type': strategy_type,
                'selected_strategy': selected_strategy
            }
        )
        return self.load_strategy_return_value

    def load_radiomics_params_file(self) -> Optional[str]:
        self.load_radiomics_params_file_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.load_radiomics_params_file_return_value

    def load_database_type(self) -> str:
        self.load_database_type_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.load_database_type_return_value

    def get_save_database_settings_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_database_settings_called_with_parameters

    def set_save_database_settings_return_value(self, return_value: Any) -> None:
        self.save_data_directory_return_value = return_value

    def get_load_database_settings_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.load_database_settings_called_with_parameters

    def set_load_database_settings_return_value(self, return_value: Any) -> None:
        self.load_database_settings_return_value = return_value

    def get_save_data_directory_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_data_directory_called_with_parameters

    def set_save_data_directory_return_value(self, return_value: Any) -> None:
        self.save_data_directory_return_value = return_value

    def get_load_data_directory_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.load_data_directory_called_with_parameters

    def set_load_data_directory_return_value(self, return_value: Any) -> None:
        self.load_data_directory_return_value = return_value

    def get_load_region_of_interest_selector_properties_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.load_region_of_interest_selector_properties_called_with_parameters

    def set_load_region_of_interest_selector_properties_return_value(self, return_value: Any):
        self.load_region_of_interest_selector_properties_return_value = return_value

    def get_load_strategy_selection_called_with_parameter(self) -> List[Dict[Optional[str], Any]]:
        return self.load_strategy_selection_called_with_parameters

    def set_load_strategy_selection_return_value(self, return_value: Any):
        self.load_strategy_selection_return_value = return_value

    def get_load_strategy_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.load_strategy_called_with_parameters

    def set_load_strategy_return_value(self, return_value: Any):
        self.load_strategy_return_value = return_value

    def get_load_radiomics_params_file_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.load_radiomics_params_file_called_with_parameters

    def set_load_radiomics_params_file_return_value(self, return_value: Any) -> None:
        self.load_radiomics_params_file_return_value = return_value

    def get_load_database_type_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.load_database_type_called_with_parameters

    def set_load_database_type_return_value(self, return_value: Any) -> None:
        self.load_database_type_return_value = return_value
