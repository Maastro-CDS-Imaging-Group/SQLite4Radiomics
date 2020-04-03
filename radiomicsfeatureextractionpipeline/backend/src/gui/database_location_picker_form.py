import tkinter as tk
from tkinter import filedialog

import pygubu

from logic.logic import Logic


class DatabaseLocationPickerForm(tk.Frame):
    """
    Manages the data database location picker form.
    This form is used for selecting the location of the database that will be used for storage.
    """

    def __init__(self, logic: Logic, parent: tk.Frame, controller: tk.Tk) -> None:
        self.logic: Logic = logic
        tk.Frame.__init__(self, parent)
        self.controller: tk.Tk = controller
        controller.winfo_toplevel().title("Radiomic Feature Extraction")
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('../gui_prefabs/database_location_picker_form.ui')
        self.main_screen: tk.Frame = builder.get_object('database_location_picker_form', self)
        builder.connect_callbacks(self)

    def select_database_file(self) -> None:
        print('Browse')
        database_location: str = filedialog.askopenfilename(filetypes=[("SQLite3 Database", "*.db3")])
        print(database_location)
        text_entry: tk.Text = self.builder.get_object("text_entry_connection_string")
        text_entry.insert(0, database_location)

    def connect_with_database(self) -> None:
        text_entry: tk.Text = self.builder.get_object("text_entry_connection_string")
        if not text_entry.get():
            return
        self.logic.set_database_connection_string(text_entry.get())
        self.controller.quit()
