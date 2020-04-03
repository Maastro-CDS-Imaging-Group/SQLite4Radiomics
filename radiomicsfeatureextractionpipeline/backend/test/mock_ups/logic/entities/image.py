from typing import Optional, List, Dict, Any

import pydicom

from logic.entities.image import Image


class ImageMockUp(Image):

    def __init__(self, instance: str, class_ui: str, number: str, date: str, times: str, echo_number: str,
                 number_of_frames: str, acq_date: str, acq_time: str, receiving_c: str, acq_number: str,
                 slice_location: str, samples_per: str, photo_metric: str, rows: str, columns: str, bits_stored: str,
                 image_type: str, identity: str, object_file: str, device_name: str,
                 content: pydicom.FileDataset = None):
        super().__init__(instance, class_ui, number, date, times, echo_number, number_of_frames, acq_date, acq_time,
                         receiving_c, acq_number, slice_location, samples_per, photo_metric, rows, columns, bits_stored,
                         image_type, identity, object_file, device_name, content)

        self.get_instance_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_instance_return_value: Any = None

        self.set_instance_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_instance_return_value: Any = None

        self.get_class_ui_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_class_ui_return_value: Any = None

        self.set_class_ui_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_class_ui_return_value: Any = None

        self.get_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_number_return_value: Any = None

        self.set_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_number_return_value: Any = None

        self.get_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_date_return_value: Any = None

        self.set_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_date_return_value: Any = None

        self.get_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_time_return_value: Any = None

        self.set_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_time_return_value: Any = None

        self.get_echo_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_echo_number_return_value: Any = None

        self.set_echo_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_echo_number_return_value: Any = None

        self.get_number_of_frames_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_number_of_frames_return_value: Any = None

        self.set_number_of_frames_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_number_of_frames_return_value: Any = None

        self.get_acq_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_acq_date_return_value: Any = None

        self.set_acq_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_acq_date_return_value: Any = None

        self.get_acq_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_acq_time_return_value: Any = None

        self.set_acq_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_acq_time_return_value: Any = None

        self.get_receiving_c_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_receiving_c_return_value: Any = None

        self.set_receiving_c_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_receiving_c_return_value: Any = None

        self.get_acq_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_acq_number_return_value: Optional[str] = None

        self.set_acq_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_acq_number_return_value: Any = None

        self.get_slice_location_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_slice_location_return_value: Any = None

        self.set_slice_location_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_slice_location_return_value: Any = None

        self.get_samples_per_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_samples_per_return_value: Any = None

        self.set_samples_per_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_samples_per_return_value: Any = None

        self.get_photo_metric_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_photo_metric_return_value: Any = None

        self.set_photo_metric_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_photo_metric_return_value: Any = None

        self.get_rows_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_rows_return_value: Any = None

        self.set_rows_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_rows_return_value: Any = None

        self.get_columns_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_columns_return_value: Any = None

        self.set_columns_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_columns_return_value: Any = None

        self.get_bits_stored_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_bits_stored_return_value: Any = None

        self.set_bits_stored_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_bits_stored_return_value: Any = None

        self.get_image_type_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_image_type_return_value: Any = None

        self.set_image_type_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_image_type_return_value: Any = None

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_identity_return_value: Any = None

        self.get_object_file_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_object_file_return_value: Any = None

        self.set_object_file_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_object_file_return_value: Any = None

        self.get_device_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_device_name_return_value: Any = None

        self.set_device_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_device_name_return_value: Any = None

        self.get_content_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_content_return_value: Any = None

        self.set_content_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_content_return_value: Any = None

    @property
    def instance(self) -> str:
        self.get_instance_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_instance_return_value

    @instance.setter
    def instance(self, value: str) -> None:
        self.set_instance_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def class_ui(self) -> str:
        self.get_class_ui_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_class_ui_return_value

    @class_ui.setter
    def class_ui(self, value: str) -> None:
        self.set_class_ui_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def number(self) -> str:
        self.get_number_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_number_return_value

    @number.setter
    def number(self, value: str) -> None:
        self.set_number_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def date(self) -> str:
        self.get_date_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_date_return_value

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
    def echo_number(self) -> str:
        self.get_echo_number_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_echo_number_return_value

    @echo_number.setter
    def echo_number(self, value: str) -> None:
        self.set_echo_number_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def number_of_frames(self) -> str:
        self.get_number_of_frames_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_number_of_frames_return_value

    @number_of_frames.setter
    def number_of_frames(self, value: str) -> None:
        self.set_number_of_frames_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def acq_date(self) -> str:
        self.get_acq_date_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_acq_date_return_value

    @acq_date.setter
    def acq_date(self, value: str) -> None:
        self.set_acq_date_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def acq_time(self) -> str:
        self.get_acq_time_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_acq_time_return_value

    @acq_time.setter
    def acq_time(self, value: str) -> None:
        self.set_acq_time_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def receiving_c(self) -> str:
        self.get_receiving_c_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_receiving_c_return_value

    @receiving_c.setter
    def receiving_c(self, value: str) -> None:
        self.set_receiving_c_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def acq_number(self) -> str:
        self.get_acq_number_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_acq_number_return_value

    @acq_number.setter
    def acq_number(self, value: str) -> None:
        self.set_acq_number_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def slice_location(self) -> str:
        self.get_slice_location_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_slice_location_return_value

    @slice_location.setter
    def slice_location(self, value: str) -> None:
        self.set_slice_location_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def samples_per(self) -> str:
        self.get_samples_per_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_samples_per_return_value

    @samples_per.setter
    def samples_per(self, value: str) -> None:
        self.set_samples_per_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def photo_metric(self) -> str:
        self.get_photo_metric_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_photo_metric_return_value

    @photo_metric.setter
    def photo_metric(self, value: str) -> None:
        self.set_photo_metric_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def rows(self) -> str:
        self.get_rows_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_rows_return_value

    @rows.setter
    def rows(self, value: str) -> None:
        self.set_rows_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def columns(self) -> str:
        self.get_columns_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_columns_return_value

    @columns.setter
    def columns(self, value: str) -> None:
        self.set_columns_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def bits_stored(self) -> str:
        self.get_bits_stored_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_bits_stored_return_value

    @bits_stored.setter
    def bits_stored(self, value: str) -> None:
        self.set_bits_stored_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def image_type(self) -> str:
        self.get_image_type_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_image_type_return_value

    @image_type.setter
    def image_type(self, value: str) -> None:
        self.set_image_type_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def identity(self) -> str:
        self.get_identity_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_identity_return_value

    @identity.setter
    def identity(self, value: str) -> None:
        self.set_identity_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def object_file(self) -> str:
        self.get_object_file_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_object_file_return_value

    @object_file.setter
    def object_file(self, value: str) -> None:
        self.set_object_file_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def device_name(self) -> str:
        self.get_device_name_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_device_name_return_value

    @device_name.setter
    def device_name(self, value: str) -> None:
        self.set_device_name_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def content(self) -> pydicom.FileDataset:
        self.get_content_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_content_return_value

    @content.setter
    def content(self, value: pydicom.FileDataset) -> None:
        self.set_content_called_with_parameters.append(
            {
                'value': value
            }
        )

    def get_get_instance_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_instance_called_with_parameters

    def set_get_instance_return_value(self, return_value: Any) -> None:
        self.get_instance_return_value = return_value

    def get_set_instance_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_instance_called_with_parameters

    def get_set_instance_return_value(self, return_value: Any) -> None:
        self.set_instance_return_value = return_value

    def _get_get_class_ui_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_class_ui_called_with_parameters

    def set_get_class_ui_return_value(self, return_value: Any) -> None:
        self.get_class_ui_return_value = return_value

    def get_set_class_ui_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_class_ui_called_with_parameters

    def set_set_class_ui_return_value(self, return_value: Any) -> None:
        self.set_class_ui_return_value = return_value

    def get_get_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_number_called_with_parameters

    def set_get_number_return_value(self, return_value: Any) -> None:
        self.get_number_return_value = return_value

    def get_set_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_number_called_with_parameters

    def set_set_number_return_value(self, return_value: Any) -> None:
        self.set_number_return_value = return_value

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

    def get_get_echo_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_echo_number_called_with_parameters

    def set_get_echo_number_return_value(self, return_value: Any) -> None:
        self.get_echo_number_return_value = return_value

    def get_set_echo_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_echo_number_called_with_parameters

    def set_set_echo_number_return_value(self, return_value: Any) -> None:
        self.set_echo_number_return_value = return_value

    def get_get_number_of_frames_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_number_of_frames_called_with_parameters

    def set_get_number_of_frames_return_value(self, return_value: Any) -> None:
        self.get_number_of_frames_return_value = return_value

    def get_set_number_of_frames_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_number_of_frames_called_with_parameters

    def set_set_number_of_frames_return_value(self, return_value: Any) -> None:
        self.set_number_of_frames_return_value = return_value

    def get_get_acq_date_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_acq_date_called_with_parameters

    def set_get_acq_date_return_value(self, return_value: Any) -> None:
        self.get_acq_date_return_value = return_value

    def get_set_acq_date_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_acq_date_called_with_parameters

    def set_set_acq_date_return_value(self, return_value: Any) -> None:
        self.set_acq_date_return_value = return_value

    def get_get_acq_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_acq_time_called_with_parameters

    def set_get_acq_time_return_value(self, return_value: Any) -> None:
        self.get_acq_time_return_value = return_value

    def get_set_acq_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_acq_time_called_with_parameters

    def set_set_acq_time_return_value(self, return_value: Any) -> None:
        self.set_acq_time_return_value = return_value

    def get_get_receiving_c_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_receiving_c_called_with_parameters

    def set_get_receiving_c_return_value(self, return_value: Any) -> None:
        self.get_receiving_c_return_value = return_value

    def get_set_receiving_c_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_receiving_c_called_with_parameters

    def set_set_receiving_c_return_value(self, return_value: Any) -> None:
        self.set_receiving_c_return_value = return_value

    def get_get_acq_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_acq_number_called_with_parameters

    def set_get_acq_number_return_value(self, return_value: Any) -> None:
        self.get_acq_number_return_value = return_value

    def get_set_acq_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_acq_number_called_with_parameters

    def set_set_acq_number_return_value(self, return_value: Any) -> None:
        self.set_acq_number_return_value = return_value

    def get_get_slice_location_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_slice_location_called_with_parameters

    def set_get_slice_location_return_value(self, return_value: Any) -> None:
        self.get_slice_location_return_value = return_value

    def get_set_slice_location_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_slice_location_called_with_parameters

    def set_set_slice_location_return_value(self, return_value: Any) -> None:
        self.set_slice_location_return_value = return_value

    def get_get_samples_per_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_samples_per_called_with_parameters

    def set_get_samples_per_return_value(self, return_value: Any) -> None:
        self.get_samples_per_return_value = return_value

    def get_set_samples_per_called_by_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_samples_per_called_with_parameters

    def set_set_samples_per_return_value(self, return_value: Any) -> None:
        self.set_samples_per_return_value = return_value

    def get_get_photo_metric_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_photo_metric_called_with_parameters

    def set_get_photo_metric_return_value(self, return_value: Any) -> None:
        self.get_photo_metric_return_value = return_value

    def get_set_photo_metric_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_photo_metric_called_with_parameters

    def set_set_photo_metric_return_value(self, return_value: Any) -> None:
        self.set_photo_metric_return_value = return_value

    def get_get_rows_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_rows_called_with_parameters

    def set_get_rows_return_value(self, return_value: Any) -> None:
        self.get_rows_return_value = return_value

    def get_set_rows_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_rows_called_with_parameters

    def set_set_rows_return_value(self, return_value: Any) -> None:
        self.set_rows_return_value = return_value

    def get_get_columns_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_columns_called_with_parameters

    def set_get_columns_return_value(self, return_value: Any) -> None:
        self.get_columns_return_value = return_value

    def get_set_columns_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_columns_called_with_parameters

    def set_set_columns_return_value(self, return_value: Any) -> None:
        self.set_columns_return_value = return_value

    def get_get_bits_stored_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_bits_stored_called_with_parameters

    def set_get_bits_stored_return_value(self, return_value: Any) -> None:
        self.get_bits_stored_return_value = return_value

    def get_set_bits_stored_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_bits_stored_called_with_parameters

    def set_set_bits_stored_return_value(self, return_value: Any) -> None:
        self.set_bits_stored_return_value = return_value

    def get_get_image_type_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_image_type_called_with_parameters

    def set_get_image_type_return_type(self, return_type: Any) -> None:
        self.get_image_type_return_value = return_type

    def get_set_image_type_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_image_type_called_with_parameters

    def set_set_image_type_return_type(self, return_value: Any) -> None:
        self.set_image_type_return_value = return_value

    def get_get_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_identity_called_with_parameters

    def set_get_identity_result_value(self, result_value: Any) -> None:
        self.get_identity_return_value = result_value

    def get_set_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_identity_called_with_parameters

    def set_set_identity_return_value(self, return_value: Any) -> None:
        self.set_identity_return_value = return_value

    def get_get_object_file_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_object_file_called_with_parameters

    def set_get_object_file_return_value(self, return_value: Any) -> None:
        self.get_object_file_return_value = return_value

    def get_set_object_file_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_object_file_called_with_parameters

    def set_set_object_file_return_value(self, return_value: Any) -> None:
        self.set_object_file_return_value = return_value

    def get_get_device_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_device_name_called_with_parameters

    def set_get_device_name_return_value(self, return_value: Any) -> None:
        self.get_device_name_return_value = return_value

    def get_set_device_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_device_name_called_with_parameters

    def set_set_device_name_return_value(self, return_value: Any) -> None:
        self.set_device_name_return_value = return_value

    def get_get_content_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_content_called_with_parameters

    def set_get_content_return_value(self, return_value: Any) -> None:
        self.get_content_return_value: Any = return_value

    def get_set_content_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_content_called_with_parameters

    def set_set_content_return_value(self, return_value: str) -> None:
        self.set_content_called_with_parameters = return_value
