from typing import Optional, List, Dict, Any

from cli.radiomic_feature_extraction_pipeline_cli import CLI
from logic.logic import Logic


class CLIMockUp(CLI):

    def __init__(self, logic: Logic) -> None:
        super().__init__(logic)

        self.start_extraction_pipeline_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.start_extraction_pipeline_return_value: Any = None

        self.start_priority_setter_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.start_priority_setter_return_value: Any = None

    def start_extraction_pipeline(self, sop_instance_rtstruct: str) -> None:
        self.start_extraction_pipeline_called_with_parameters.append(
            {
                'sop_instance_rtstruct': sop_instance_rtstruct
            }
        )
        return self.start_extraction_pipeline_return_value

    def start_priority_setter(self) -> None:
        self.start_priority_setter_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.start_priority_setter_return_value

    def get_start_extraction_pipeline_called_with_parameters(self) -> List[Dict[str, Any]]:
        return self.start_extraction_pipeline_called_with_parameters

    def set_start_extraction_pipeline_return_value(self, return_value: Any) -> None:
        self.start_extraction_pipeline_return_value = return_value

    def get_start_priority_setter_called_with_parameters(self) -> List[Dict[str, Any]]:
        return self.start_priority_setter_called_with_parameters

    def set_start_priority_setter_return_value(self, return_value: Any):
        self.start_priority_setter_return_value = return_value