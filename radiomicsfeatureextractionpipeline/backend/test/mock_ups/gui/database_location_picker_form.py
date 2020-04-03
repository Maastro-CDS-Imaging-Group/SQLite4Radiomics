import tkinter as tk
from typing import Any, Optional, Dict, List

from gui.database_location_picker_form import DatabaseLocationPickerForm
from logic.logic import Logic


class DatabaseLocationPickerFormMockUp(DatabaseLocationPickerForm):

    def __init__(self, logic: Logic, parent: tk.Frame, controller: tk.Tk):
        super().__init__(logic, parent, controller)

        self.select_database_file_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.select_database_file_return_value: Any = None

        self.connect_with_database_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.connect_with_database_return_value: Any = None

    def select_database_file(self) -> None:
        self.select_database_file_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.select_database_file_return_value

    def connect_with_database(self) -> None:
        self.connect_with_database_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.connect_with_database_return_value

    def get_select_database_file_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.select_database_file_called_with_parameters

    def set_select_database_file_return_value(self, return_value: Any) -> None:
        self.select_database_file_return_value = return_value

    def get_connect_with_database_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.connect_with_database_called_with_parameters

    def set_connect_with_database_return_value(self, return_value: Any) -> None:
        self.connect_with_database_return_value = return_value
