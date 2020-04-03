import tkinter as tk
from typing import Any, Optional, Dict, List

from gui.main_screen_form import MainScreenForm
from logic.logic import Logic


class MainScreenFormMockUp(MainScreenForm):

    def __init__(self, logic: Logic, parent: tk.Frame, controller: tk.Tk) -> None:
        super().__init__(logic, parent, controller)

        self.update_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.update_return_value: Any = None

        self.fill_tree_view_with_patients_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.fill_tree_view_with_patients_return_value: Any = None

    def update(self) -> None:
        self.update_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.update_return_value

    def fill_tree_view_with_patients(self) -> None:
        self.fill_tree_view_with_patients_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.fill_tree_view_with_patients_return_value

    def get_update_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.update_called_with_parameters

    def set_update_return_value(self, return_value: Any) -> None:
        self.update_return_value = return_value

    def get_fill_tree_view_patients_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.fill_tree_view_with_patients_called_with_parameters

    def set_fill_tree_view_patients_return_value(self, return_value: Any) -> None:
        self.fill_tree_view_with_patients_return_value = return_value