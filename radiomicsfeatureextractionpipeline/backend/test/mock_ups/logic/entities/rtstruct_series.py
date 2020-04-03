from typing import Optional, Any, Dict, List

from logic.entities.image import Image
from logic.entities.rtstruct_series import RtstructSeries
from test.mock_ups.logic.entities.series import SeriesMockUp


class RtstructSeriesMockUp(RtstructSeries, SeriesMockUp):

    def __init__(self, identity: str, number: str, modality: str, manufacture: str, model_name: str,
                 patient_position: str, image: Image = None):
        super().__init__(identity, number, modality, manufacture, model_name, patient_position, image)

        self.get_image_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_image_return_value: Any = None

        self.set_image_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_image_return_value: Any = None

    @property
    def image(self) -> Image:
        self.get_image_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_image_return_value

    @image.setter
    def image(self, value: Image) -> None:
        self.get_image_called_with_parameters.append(
            {
                'value': value
            }
        )

    def get_get_image_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_image_called_with_parameters

    def set_get_image_return_value(self, return_value: Any) -> None:
        self.get_image_return_value = return_value

    def get_set_image_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_image_called_with_parameters

    def set_set_image_return_value(self, return_value: Any) -> None:
        self.set_image_return_value = return_value
