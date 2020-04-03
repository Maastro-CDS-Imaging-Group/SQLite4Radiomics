import tkinter as tk
from tkinter import filedialog

import pygubu

from logic.logic import Logic


class DataDirectorySelectorForm(tk.Frame):
    """
    Manages the data directory selector form
    This form is used for selecting the directory where all dicom files are stored.
    """

    def __init__(self, logic: Logic, parent: tk.Frame, controller: tk.Tk) -> None:
        self.logic: Logic = logic
        tk.Frame.__init__(self, parent)
        self.controller: tk.Tk = controller
        controller.winfo_toplevel().title("Radiomic Feature Extraction")
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('../gui_prefabs/data_directory_selector_form.ui')
        self.main_screen: tk.Frame = builder.get_object('data_directory_selector_form', self)
        builder.connect_callbacks(self)

    def select_dicom_data_directory(self) -> None:
        print('Browse')
        dicom_directory_location: str = filedialog.askdirectory(parent=self, initialdir="/")
        print(dicom_directory_location)
        text_entry: tk.Text = self.builder.get_object("text_entry_root_directory_dicom")
        text_entry.insert(0, dicom_directory_location)

    def save_configuration(self) -> None:
        text_entry: tk.Text = self.builder.get_object("text_entry_root_directory_dicom")
        if not text_entry.get():
            return
        self.logic.set_dicom_data_directory(text_entry.get())
        self.controller.quit()

