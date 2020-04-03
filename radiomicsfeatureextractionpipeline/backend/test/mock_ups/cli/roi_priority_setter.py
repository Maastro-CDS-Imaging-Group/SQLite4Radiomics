from typing import List, Dict, Optional, Any

from cli.roi_priority_setter import ROIPrioritySetter
from logic.logic import Logic


class ROIPrioritySetterMockUp(ROIPrioritySetter):

    def __init__(self, logic: Logic) -> None:
        super().__init__(logic)

        self.set_rois_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_rois_return_value: Any = None

    def set_rois(self) -> None:
        self.set_rois_called_with_parameters.append(
            {
                None: None
            }
        )

        return self.set_rois_return_value

    def get_set_rois_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_rois_called_with_parameters

    def set_set_rois_return_value(self, return_value: Any) -> None:
        self.set_rois_return_value = return_value
