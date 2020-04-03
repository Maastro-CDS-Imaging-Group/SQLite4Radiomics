from typing import List, Optional, Any, Dict

from logic.entities.image import Image
from logic.entities.series_with_image_slices import SeriesWithImageSlices
from test.mock_ups.logic.entities.series import SeriesMockUp


class SeriesWithImageSlicesMockUp(SeriesWithImageSlices, SeriesMockUp):

    def __init__(self, identity:str, number: str, modality: str, manufacture: str, model_name: str,
                 patient_position: str, date: str, time: str, description: str, body_part_ex: str, protocol_name: str,
                 institution: str, frame_of_reference: str, images: List[Image] = None) -> None:
        super().__init__(identity, number, modality, manufacture, model_name, patient_position, date, time, description,
                         body_part_ex, protocol_name, institution, frame_of_reference, images)

        self.get_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_date_return_value: Any = None

        self.set_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_date_return_value: Any = None

        self.get_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_time_return_value: Any = None

        self.set_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_time_return_value: Any = None

        self.get_description_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_description_return_value: Any = None

        self.set_description_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_description_return_value: Any = None

        self.get_body_part_ex_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_body_part_ex_return_value: Any = None

        self.set_body_part_ex_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_body_part_ex_return_value: Any = None

        self.get_protocol_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_protocol_name_return_value: Any = None

        self.set_protocol_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_protocol_name_return_value: Any = None

        self.get_institution_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_institution_return_value: Any = None

        self.set_institution_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_institution_return_value: Any = None

        self.get_frame_of_reference_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_frame_of_reference_return_value: Any = None

        self.set_frame_of_reference_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_frame_of_reference_return_value: Any = None

        self.get_images_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_images_return_value: Any = None

        self.set_images_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_images_return_value: Any = None

        self.add_image_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.add_image_return_value: Any = None

        self.remove_image_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.remove_image_return_value: Any = None

    @property
    def date(self) -> str:
        self.get_date_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_time_return_value

    @date.setter
    def date(self, value: str) -> None:
        self.set_date_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def time(self) -> str:
        self.get_time_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_time_return_value

    @time.setter
    def time(self, value: str) -> None:
        self.set_time_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def description(self) -> str:
        self.get_description_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_description_return_value

    @description.setter
    def description(self, value: str) -> None:
        self.set_description_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def body_part_ex(self) -> str:
        self.get_body_part_ex_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_body_part_ex_return_value

    @body_part_ex.setter
    def body_part_ex(self, value: str) -> None:
        self.set_body_part_ex_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def protocol_name(self) -> str:
        self.get_protocol_name_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_protocol_name_return_value

    @protocol_name.setter
    def protocol_name(self, value: str) -> None:
        self.set_protocol_name_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def institution(self) -> str:
        self.get_institution_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_institution_return_value

    @institution.setter
    def institution(self, value: str) -> None:
        self.set_institution_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def frame_of_reference(self) -> str:
        self.get_frame_of_reference_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_frame_of_reference_return_value

    @frame_of_reference.setter
    def frame_of_reference(self, value: str) -> None:
        self.set_frame_of_reference_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def images(self) -> List[Image]:
        self.get_images_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_images_return_value

    @images.setter
    def images(self, value: List[Image]) -> None:
        self.set_images_called_with_parameters.append(
            {
                'value': value
            }
        )

    def add_image(self, image: Image) -> None:
        self.add_image_called_with_parameters.append(
            {
                'image': image
            }
        )
        return self.add_image_return_value

    def remove_image(self, image: Image) -> None:
        self.remove_image_called_with_parameters.append(
            {
                'image': image
            }
        )
        return self.remove_image_return_value

    def get_get_date_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_date_called_with_parameters

    def set_get_date_return_value(self, return_value: Any) -> None:
        self.get_date_return_value = return_value

    def get_set_date_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_date_called_with_parameters

    def set_set_date_return_value(self, return_value: Any) -> None:
        self.set_date_return_value = return_value

    def get_get_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_time_called_with_parameters

    def set_get_time_return_value(self, return_value: Any) -> None:
        self.get_time_return_value = return_value

    def get_set_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_time_called_with_parameters

    def set_set_time_return_value(self, return_value: Any) -> None:
        self.set_time_return_value = return_value

    def get_get_description_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_description_called_with_parameters

    def set_get_description_return_value(self, return_value: Any) -> None:
        self.get_description_return_value = return_value

    def get_set_description_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_description_called_with_parameters

    def set_set_description_return_value(self, return_value: Any) -> None:
        self.set_description_return_value = return_value

    def get_get_body_part_ex_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_body_part_ex_called_with_parameters

    def set_get_body_part_ex_return_value(self, return_value: Any) -> None:
        self.get_body_part_ex_return_value = return_value

    def get_set_body_part_ex_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_body_part_ex_called_with_parameters

    def set_set_body_part_ex_return_value(self, return_value: Any) -> None:
        self.set_body_part_ex_return_value = return_value

    def get_get_protocol_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_protocol_name_called_with_parameters

    def set_get_protocol_name_is_called(self, return_value: Any) -> None:
        self.get_protocol_name_return_value = return_value

    def get_set_protocol_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_protocol_name_called_with_parameters

    def set_set_protocol_name_return_value(self, return_value: Any) -> None:
        self.set_protocol_name_return_value = return_value

    def get_get_institution_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_institution_called_with_parameters

    def set_get_institution_return_value(self, return_value: Any) -> None:
        self.get_institution_return_value = return_value

    def get_set_institution_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_institution_called_with_parameters

    def set_set_institution_return_value(self, return_value: Any) -> None:
        self.set_institution_return_value = return_value

    def get_get_frame_of_reference_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_frame_of_reference_called_with_parameters

    def set_get_frame_of_reference_return_value(self, return_value: Any) -> None:
        self.get_frame_of_reference_return_value = return_value

    def get_set_frame_of_reference_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_frame_of_reference_called_with_parameters

    def set_set_frame_of_reference_return_value(self, return_value: Any) -> None:
        self.set_frame_of_reference_return_value = return_value

    def get_get_images_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_images_called_with_parameters

    def set_get_images_return_value(self, return_value: Any) -> None:
        self.get_images_return_value = return_value

    def get_set_images_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_images_called_with_parameters

    def set_set_images_return_value(self, return_value: Any) -> None:
        self.set_images_return_value = return_value

    def get_add_image_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.add_image_called_with_parameters

    def set_add_image_return_value(self, return_value: Any) -> None:
        self.add_image_return_value = return_value

    def get_remove_image_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.remove_image_called_with_parameters

    def set_remove_image_return_value(self, return_value: Any) -> None:
        self.remove_image_return_value = return_value
