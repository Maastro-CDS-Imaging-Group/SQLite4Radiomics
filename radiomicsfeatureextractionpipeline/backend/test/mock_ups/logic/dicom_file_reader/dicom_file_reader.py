from typing import Optional, List, Any, Dict

from logic.dicom_file_reader.dicom_file_reader import DicomFileReader
from logic.entities.image import Image


class DicomFileReaderMockUp(DicomFileReader):

    def __init__(self, dicom_data_directory: str) -> None:
        super().__init__(dicom_data_directory)

        self.set_dicom_directory_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_dicom_directory_return_value: Any = None

        self.read_dicom_file_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.read_dicom_file_return_value: Any = None

        self.read_multiple_dicom_files_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.read_multiple_dicom_files_return_value: Any = None

    def set_dicom_data_directory(self, dicom_data_directory: str) -> None:
        self.set_dicom_directory_called_with_parameters.append(
            {
                'dicom_data_directory': dicom_data_directory
            }
        )
        return self.set_dicom_directory_return_value

    def read_dicom_file(self, image: Image) -> Optional[Image]:
        self.read_dicom_file_called_with_parameters.append(
            {
                'image': image
            }
        )
        return self.read_dicom_file_return_value

    def read_multiple_dicom_files(self, images: List[Image]) -> Optional[List[Image]]:
        self.read_multiple_dicom_files_called_with_parameters.append(
            {
                'images': images
            }
        )
        return self.read_multiple_dicom_files_return_value

    def get_set_dicom_file_directory_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_dicom_directory_called_with_parameters

    def set_set_dicom_file_directory_return_value(self, return_value: Any):
        self.set_dicom_directory_return_value = return_value

    def get_read_dicom_file_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.read_dicom_file_called_with_parameters

    def set_read_dicom_file_return_value(self, return_value: Any) -> None:
        self.read_dicom_file_return_value = return_value

    def get_read_multiple_dicom_files_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.read_multiple_dicom_files_called_with_parameters

    def set_read_multiple_dicom_files_return_value(self, return_value: Any) -> None:
        self.read_multiple_dicom_files_return_value = return_value
