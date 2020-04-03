from typing import Any, Dict, Tuple, Optional, List

import SimpleITK as sitk
import numpy as np
import pydicom

from logic.binary_mask_and_3d_image_generator.binary_mask_generator import BinaryMaskGenerator
from logic.entities.image import Image
from test.mock_ups.logic.binary_mask_and_3d_image_generator.binary_mask_and_3d_image_generator import \
    BinaryMaskAnd3DImageGeneratorMockUp


class BinaryMaskGeneratorMockUp(BinaryMaskGenerator, BinaryMaskAnd3DImageGeneratorMockUp):

    get_pixels_called_with_parameters: List[Dict[Optional[str], Any]] = []
    get_pixels_return_value: Any = None

    create_mask_from_rtstruct_called_with_parameters: List[Dict[Optional[str], Any]] = []
    create_mask_from_rtstruct_return_value: Any = None

    def __init__(self):
        super().__init__()

        self.image_pre_processing_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.image_pre_processing_return_value: Any = None

        self.image_pre_processing_ct_and_pet_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.image_pre_processing_ct_and_pet_return_value: Any = None

        self.image_pre_processing_mri_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.image_pre_processing_mri_return_value: Any = None

    def image_pre_processing(
            self, images_slices: List[Image], rtstruct_image: Image, roi_number: int, npat: str = '',
            convert: bool = False, export_directory: str = '') -> Tuple[sitk.Image, sitk.Image]:
        self.image_pre_processing_called_with_parameters.append(
            {
                'images_slices': images_slices,
                'rtstruct_image': rtstruct_image,
                'roi_number': roi_number,
                'npat': npat,
                'convert': convert,
                'export_directory': export_directory
            }
        )
        return self.image_pre_processing_return_value

    def image_pre_processing_ct_and_pet(
            self, content_first_image: pydicom.FileDataset, roi_number: int, num_slice: int, image_slices: List[Image],
            content_rtstruct: pydicom.FileDataset, resolution_x: np.ndarray, resolution_y: np.ndarray, IM_P: np.ndarray,
            mask: np.ndarray) -> Optional[np.ndarray]:
        self.image_pre_processing_ct_and_pet_called_with_parameters.append(
            {
                'content_first_image': content_first_image,
                'roi_number': roi_number,
                'num_slice': num_slice,
                'image_slices': image_slices,
                'content_rtstruct': content_rtstruct,
                'resolution_x': resolution_x,
                'resolution_y': resolution_y,
                'IM_P': IM_P,
                'mask': mask
            }
        )
        return self.image_pre_processing_ct_and_pet_return_value

    def image_pre_processing_mri(self) -> Optional[np.ndarray]:
        self.image_pre_processing_mri_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.image_pre_processing_mri_return_value

    @staticmethod
    def get_pixels(image_slices: List[Image]) -> np.array:
        BinaryMaskGeneratorMockUp.get_pixels_called_with_parameters.append(
            {
                'image_slices': image_slices
            }
        )
        return BinaryMaskGeneratorMockUp.get_pixels_return_value

    @staticmethod
    def create_mask_from_rtstruct(vertex_row_coordinates: np.ndarray, vertex_col_coordinates: np.ndarray,
                                  shape: List[int]) -> np.ndarray:
        BinaryMaskGeneratorMockUp.create_mask_from_rtstruct_called_with_parameters.append(
            {
                'vertex_row_coordinates': vertex_row_coordinates,
                'vertex_col_coordinates': vertex_col_coordinates,
                'shape': shape
            }
        )
        return BinaryMaskGeneratorMockUp.create_mask_from_rtstruct_return_value

    def get_image_pre_processing_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.image_pre_processing_called_with_parameters

    def set_image_pre_processing_return_value(self, return_value: Any) -> None:
        self.image_pre_processing_return_value = return_value

    def get_image_pre_processing_ct_and_pet_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.image_pre_processing_ct_and_pet_called_with_parameters

    def set_image_pre_processing_ct_and_pet_return_value(self, return_value: Any) -> None:
        self.image_pre_processing_ct_and_pet_return_value = return_value

    def get_image_pre_processing_mri_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.image_pre_processing_mri_called_with_parameters

    def set_image_pre_processing_mri_return_value(self, return_value: Any) -> None:
        self.image_pre_processing_mri_return_value = return_value

    def get_get_pixels_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_pixels_called_with_parameters

    def set_get_pixels_return_value(self, return_value: Any) -> None:
        self.get_pixels_return_value = return_value

    def get_create_mask_from_rtstruct_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.create_mask_from_rtstruct_called_with_parameters

    def set_create_mask_from_rtstruct_return_value(self, return_value: np.ndarray) -> None:
        self.create_mask_from_rtstruct_return_value = return_value
