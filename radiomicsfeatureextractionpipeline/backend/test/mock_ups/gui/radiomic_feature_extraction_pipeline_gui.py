from typing import Optional, Any, Dict, List

from gui.radiomic_feature_extraction_pipeline_gui import GUI
from logic.logic import Logic


class GUIMockUp(GUI):

    def __init__(self, logic: Logic) -> None:
        super().__init__(logic)

        self.show_frame_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.show_frame_return_value: Any = None

        self.database_location_selector_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.database_location_selector_return_value: Any = None

        self.data_directory_selector_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.data_directory_selector_return_value: Any = None

        self.show_main_screen_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.show_main_screen_return_value: Any = None

        self.start_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.start_return_value: Any = None

    def show_frame(self, page_name: str) -> None:
        self.show_frame_called_with_parameters.append(
            {
                'page_name': page_name
            }
        )
        return self.show_frame_return_value

    def database_location_selector(self) -> None:
        self.database_location_selector_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.database_location_selector_return_value

    def data_directory_selector(self) -> None:
        self.data_directory_selector_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.data_directory_selector_return_value

    def show_main_screen(self) -> None:
        self.show_main_screen_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.show_main_screen_return_value

    def start(self) -> None:
        self.start_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.start_return_value

    def get_show_frame_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.show_frame_called_with_parameters

    def set_show_frame_return_value(self, return_value: Any) -> None:
        self.show_frame_return_value = return_value

    def get_database_location_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.database_location_selector_called_with_parameters

    def set_database_location_return_value(self, return_value: Any) -> None:
        self.database_location_selector_return_value = return_value

    def get_data_directory_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.data_directory_selector_called_with_parameters

    def set_data_directory_return_value(self, return_value: Any) -> None:
        self.data_directory_selector_return_value = return_value

    def get_show_main_screen_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.show_main_screen_called_with_parameters

    def set_show_main_screen_return_value(self, return_value: Any) -> None:
        self.show_main_screen_return_value = return_value

    def get_start_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.start_called_with_parameters

    def set_start_return_value(self, return_value: Any) -> None:
        self.start_return_value = return_value
