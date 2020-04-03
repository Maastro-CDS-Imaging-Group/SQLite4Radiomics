import tkinter as tk

import pygubu

from logic.logic import Logic


class MainScreenForm(tk.Frame):
    """
    Manages the main screen form
    """
    def __init__(self, logic: Logic, parent: tk.Frame, controller: tk.Tk) -> None:
        self.logic: Logic = logic
        tk.Frame.__init__(self, parent)
        self.controller: tk.Tk = controller
        controller.winfo_toplevel().title("Radiomic Feature Extraction")
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('../gui_prefabs/main_screen_form.ui')
        self.main_screen: tk.Frame = builder.get_object('Mainframe', self)
        builder.connect_callbacks(self)
        
    def update(self) -> None:
        self.fill_tree_view_with_patients()
    
    def fill_tree_view_with_patients(self) -> None:
        pass
#        patients = self.logic.get_patient_overview()
#        tree = self.builder.get_object("treeview_patient_roi")
#        i = 1
#        for patient in patients:
#            tree.insert("", "0", "Patient" + i, text=patient['PatientID'])
