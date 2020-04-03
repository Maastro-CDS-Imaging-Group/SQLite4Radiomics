import logging
import os
from typing import List, Optional

import pydicom
from pydicom.errors import InvalidDicomError

from logic.dicom_file_reader.dicom_file_reader import DicomFileReader
from logic.entities.image import Image

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

error_logger_formatter = logging.Formatter('%(asctime)s:%(name):%(message)s')

file_handler = logging.FileHandler('logs/dicom_file_reader.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(error_logger_formatter)

debug_logger_formatter = logging.Formatter('%(asctime)s:%(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(debug_logger_formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.info('pydicom version: {0}'.format(str(pydicom.__version__)))


class BasicDicomFileReader(DicomFileReader):
    """
    Implementation of Strategy pattern for reading DICOM files
    Implements DicomFileReader class.
    """
    def __init__(self, dicom_data_directory: str = None) -> None:
        """
        Constructor BasicDicomFileReader class
        :param dicom_data_directory: The path to the directory where all DICOM files are stored
        """
        super().__init__(dicom_data_directory)

    def read_dicom_file(self, image: Image) -> Optional[Image]:
        if not os.path.isfile(self.dicom_data_directory + '\\' + image.object_file):
            logger.error('The file {} could not be found. Check the file path and try again'.format(
                self.dicom_data_directory + '\\' + image.object_file))
            return None
        try:
            image.content: pydicom.FileDataset = pydicom.dcmread(self.dicom_data_directory + '\\' + image.object_file)
        except InvalidDicomError:
            logger.exception('Something went wrong while reading the file. Try again later.')
            return None
        return image
    
    def read_multiple_dicom_files(self, images: List[Image]) -> Optional[List[Image]]:
        images_with_content: List[Image] = []
        failed_conversions: List[Image] = []

        image: Image
        for image in images:
            image_with_content: Optional[Image] = self.read_dicom_file(image)
            if image_with_content is None:
                failed_conversions.append(image)
                continue
            images_with_content.append(image_with_content)
        if len(failed_conversions) == 0:
            logger.info('All {} were converted correctly'.format(len(images_with_content)))
        else:
            logger.warning("Completed with errors! {} of the {} files weren't converted".format(
                len(failed_conversions), len(images)))

            file_path_failed: Image
            for file_path_failed in failed_conversions:
                logger.warning(type(file_path_failed))
                logger.warning(file_path_failed)
        return images_with_content
