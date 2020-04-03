"""
This module starts the Radiomic Feature Calculation Pipeline
"""

from logic.logic import Logic


class AutomaticFeatureExtractor:
    """
    This class will initialize the radiomic feature extraction pipeline.
    It expects the SOP instance of a RTSTRUCT.
    This class should be created from your command line interface
    """

    def __init__(self, logic: Logic) -> None:
        """
        Constructor of AutomaticFeatureExtractor
        :param logic: Instance of the Logic Class
        """
        self.logic: Logic = logic

    def start_calculation(self, sop_instance_rtstruct: str = None) -> None:
        """
        Starts the calculation of radiomic features.
        :param sop_instance_rtstruct: The sop instance of the rtstruct that the program will calculate the radiomic
        features for.
        :return: Method has no return value
        """
        self.logic.extract_features(sop_instance_rtstruct)

