"""
This module starts the command line interface tools.
It provides 2 tools:
-The Extraction Pipeline calculates the radiomic features for the given SOP-instance of an rtstruct.
-The Priority Setter can be used to set the priority for the ROI's that are stored in the database.
"""

from cli.automatic_feature_extractor import AutomaticFeatureExtractor
from cli.roi_priority_setter import ROIPrioritySetter
from logic.logic import Logic


class CLI:
    """
    This class will start the CLI(command line interface) tools.
    """

    def __init__(self, logic: Logic):
        """
        Constructor of the CLI.
        :param logic: Instance of the Logic.
        """
        self.automatic_feature_extractor: AutomaticFeatureExtractor = AutomaticFeatureExtractor(logic)
        self.roi_priority_setter: ROIPrioritySetter = ROIPrioritySetter(logic)

    def start_extraction_pipeline(self, sop_instance_rtstruct: str) -> None:
        """
        Starts the calculation of radiomic features.
        :param sop_instance_rtstruct: The sop instance of the rtstruct that the program will calculate the radiomic
        features for.
        :return: Method has no return value.
        """
        self.automatic_feature_extractor.start_calculation(sop_instance_rtstruct)

    def start_priority_setter(self) -> None:
        """
        Starts the priority setter tool for region of interests.
        :return: Method has no return value.
        """
        self.roi_priority_setter.set_rois()
