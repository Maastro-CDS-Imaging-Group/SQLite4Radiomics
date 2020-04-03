import tkinter as tk
from typing import Dict, Any

from gui.data_directory_selector_form import DataDirectorySelectorForm
from gui.database_location_picker_form import DatabaseLocationPickerForm
from gui.main_screen_form import MainScreenForm
from logic.logic import Logic


class GUI(tk.Tk):
    """
    Controls the Graphical user interface.
    Decides which form to show and what to do.
    """

    def __init__(self, logic: Logic) -> None:
        tk.Tk.__init__(self)

        self.logic = logic
        container: tk.Frame = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames: Dict[str, tk.Frame] = {}

        F: Any
        for F in (DatabaseLocationPickerForm, DataDirectorySelectorForm, MainScreenForm):
            page_name: str = F.__name__
            frame: tk.Frame = F(logic, container, self)
            self.frames[page_name]: Dict[str, tk.Frame] = frame

            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name: str) -> None:
        frame: tk.Frame = self.frames[page_name]
        frame.tkraise()
        frame.update()
        self.mainloop()

    def database_location_selector(self) -> None:
        """
        Shows the database location selector of the application
        :return: The method doesn't return anything.
        """

        # Shows the database location picker form of the application.
        self.show_frame("DatabaseLocationPickerForm")

    def data_directory_selector(self) -> None:
        """
        Shows the data directory selector of the application.
        :return: The method doesn't return anything.
        """

        # Shows the data directory selector form of the application.
        self.show_frame("DataDirectorySelectorForm")

    def show_main_screen(self) -> None:
        """
        Shows the main screen of the application.
        :return: The method doesn't return anything.
        """

        # Shows the main screen form of the application.
        self.show_frame("MainScreenForm")

    def start(self) -> None:
        """
        Starts the GUI application.
        :return: The method doesn't return anything.
        """

        # Shows the main screen of the application.
        self.show_main_screen()


