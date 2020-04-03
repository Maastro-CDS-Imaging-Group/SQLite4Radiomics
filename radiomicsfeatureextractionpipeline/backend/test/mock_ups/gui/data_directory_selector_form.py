import tkinter as tk
from typing import Any, Optional, Dict, List

from gui.data_directory_selector_form import DataDirectorySelectorForm
from logic.logic import Logic


class DataDirectorySelectorFormMockUp(DataDirectorySelectorForm):

    def __init__(self, logic: Logic, parent: tk.Frame, controller: tk.Tk) -> None:
        super().__init__(logic, parent, controller)

        self.select_dicom_data_directory_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.select_dicom_data_directory_return_value: Any = None

        self.save_configuration_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.save_configuration_result_value: Any = None

    def select_dicom_data_directory(self) -> None:
        self.select_dicom_data_directory_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.select_dicom_data_directory_return_value

    def save_configuration(self) -> None:
        self.save_configuration_result_value.append(
            {
                None: None
            }
        )
        return self.save_configuration_result_value

    def get_select_dicom_data_directory_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.select_dicom_data_directory_called_with_parameters

    def set_select_dicom_data_directory_return_value(self, return_value: Any) -> None:
        self.select_dicom_data_directory_return_value = return_value

    def get_save_configuration_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.save_configuration_called_with_parameters

    def set_save_configuration_return_value(self, return_value: Any) -> None:
        self.save_configuration_result_value = return_value