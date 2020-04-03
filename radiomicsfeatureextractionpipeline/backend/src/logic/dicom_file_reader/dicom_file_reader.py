from abc import ABC, abstractmethod
from typing import List, Optional

from logic.entities.image import Image


class DicomFileReader(ABC):
    """
    Abstract base class for implementation of the strategy pattern.
    Used for reading DICOM files.
    """

    def __init__(self, dicom_data_directory: str) -> None:
        """
        Constructor DicomFileReader class
        :param dicom_data_directory: The path to the directory where all DICOM files are stored
        """
        self.dicom_data_directory: str = dicom_data_directory

    def set_dicom_data_directory(self, dicom_data_directory: str) -> None:
        """
        Sets the location of the DICOM files to a new directory
        :param dicom_data_directory: The new path to the directory where all DICOM files are stored
        """
        self.dicom_data_directory: str = dicom_data_directory

    @abstractmethod
    def read_dicom_file(self, image: Image) -> Optional[Image]:
        """
        Reads the content of one single dicom file.
        :param image: The image that needs to be loaded.
        """
        pass

    @abstractmethod
    def read_multiple_dicom_files(self, images: List[Image]) -> Optional[List[Image]]:
        """
        Reads the content of multiple dicom files
        :param images: List of images that all needs to be loaded.
        """
        pass
