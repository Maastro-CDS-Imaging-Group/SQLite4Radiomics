from typing import Optional, List, Dict, Any, Tuple

from cli.automatic_feature_extractor import AutomaticFeatureExtractor
from logic.logic import Logic


class AutomaticFeatureExtractorMockUp(AutomaticFeatureExtractor):

    def __init__(self, logic: Logic) -> None:
        super().__init__(logic)
        self.start_calculation_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.start_calculation_return_value: Any = None

    def start_calculation(self, sop_instance_rtstruct: str = None) -> None:
        """
        Starts the calculation of radiomic features.
        :param sop_instance_rtstruct: The sop instance of the rtstruct that the program will calculate the radiomic
        features for.
        :return: No return type
        """
        self.start_calculation_called_with_parameters.append(
            {
                'sop_instance_rtstruct': sop_instance_rtstruct
            }
        )

        return self.start_calculation_return_value

    def get_start_calculation_called_with_parameters(self) -> List[Dict[str, Any]]:
        return self.start_calculation_called_with_parameters

    def set_start_calculation_return_value(self, return_value: Any):
        self.start_calculation_return_value = return_value
