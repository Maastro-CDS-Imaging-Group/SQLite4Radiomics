"""
This module can be used to set the priority for the ROI's that are stored in the database
"""

from typing import List

import colorama

from logic.logic import Logic
from logic.entities.roi import ROI


class ROIPrioritySetter:
    """
    This class changes the priorities of the ROI's
    """

    def __init__(self, logic: Logic) -> None:
        """
        Constructor for the ROIPrioritySetter class.
        :param logic: An instance of the Logic class.
        """
        self.logic: Logic = logic
        # Allows for different colored command line text.
        colorama.init()

    def set_rois(self) -> None:
        """
        Sets priorities for the ROI's without a set priority.
        :return: This method has no return value.
        """

        # Loads all the rois with an unset priority.
        rois: List[ROI] = self._load_unset_rois()

        # Checks if there are ROI's with an unset priority.
        if len(rois) == 0:
            # No ROI's with an unset priority found. Closing the tool.
            return

        # Shows all ROI's without a set priority.
        self._show_roi_settings(rois)

        # Sets a priority for the rois.
        self._set_priorities(rois)

        # Show all changed ROI's.
        self._show_roi_settings(rois)

        # Saves changes made to the priorities.
        self._save_changes(rois)

    def _load_unset_rois(self) -> List[ROI]:
        """
        Loads all the rois with an unset priority.
        :return: List of ROI's with an unset priority
        """

        # Get a list of undefined priorities from logic.
        rois: List[ROI] = self.logic.get_rois_with_undefined_priorities()

        # Checks if any ROI's with an undefined priority are found.
        if len(rois) != 0:
            print('\033[33;1mGive a priority between 1 and 10, 1 being Highest priority and 10 being lowest\033[0m')
            # Return the list of ROI's.
            return rois

        # Print message to screen to notify the user.
        print("No roi's found without a priority")

        # Returns an empty list.
        return []

    def _set_priorities(self, rois: List[ROI]) -> None:
        """
        Sets a priority for ROI's
        :param rois: A list of ROI's that needs to have their priority changed.
        :return: This method has no return value.
        """
        roi: ROI
        for roi in rois:
            while True:
                try:
                    # Asks the user for the new priority for the ROI.
                    # The \033[33;1m{0}\033[0m: colors the cmd text.
                    print('Set priority for roi \033[33;1m{0}\033[0m : ' .format(roi.name))
                    priority: int = int(input())
                    
                except ValueError:
                    print('\033[31;1mInvalid input! Only integer values are allowed\033[0m')
                    continue
                else:
                    # Changes the priority of the ROI.
                    if int(priority) > 0 and int(priority) <= 10:
                        roi.priority = int(priority)
                        break
                    elif int(priority) > 10 or int(priority) <= 0:
                        print('\033[31;1mPriority value out of range, please select a priority value from 1 to 10\033[0m')
                        continue
                
            
    def _show_roi_settings(self, rois: List[ROI]) -> None:
        """
        Shows a list of all the ROI in rois with their name and priority.
        :param rois: List of ROI's that will be displayed in the cmd.
        :return: This method has no return value
        """



        roi: ROI
        for roi in rois:
            # Prints all ROI's in a colored way.
            print('Name: \033[33;1m{0:20}\033[0m Priority: \033[32;1m{1}\033[0m'.format(roi.name, str(roi.priority)))

    def _save_changes(self, rois: List[ROI]) -> None:
        """
        Saves the ROI's with their new priorities or discards all the changes made to the priority.
        :param rois: List of all changed ROI's
        :return: This method has no return value.
        """

        # Asks if the user wants to save the changes.
        save_priorities: str = input("Do you want to save these priority levels? y/n")

        # Checks input user.
        if save_priorities != 'y':

            # User canceled changes and ROI's will not be saved.
            print("Configuration not saved")
            print("Canceled by user")
            return

        roi: ROI
        # Updates the priorities for the roi's
        for roi in rois:
            self.logic.update_roi_priority(roi)
        print("Successfully updated all priorities")

