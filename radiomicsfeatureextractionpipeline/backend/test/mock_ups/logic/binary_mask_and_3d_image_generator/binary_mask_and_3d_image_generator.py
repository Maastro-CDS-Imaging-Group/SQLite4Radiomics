from typing import Tuple, List, Dict, Any, Optional

import SimpleITK as sitk

from logic.binary_mask_and_3d_image_generator.binary_mask_and_3d_image_generator import BinaryMaskAnd3DImageGenerator
from logic.entities.image import Image
from logic.entities.roi import ROI


class BinaryMaskAnd3DImageGeneratorMockUp(BinaryMaskAnd3DImageGenerator):

    def __init__(self):
        self.generate_binary_mask_and_3d_image_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.generate_binary_mask_and_3d_image_return_value: Any = None

    def generate_binary_mask_and_3d_image(self, image_slices: List[Image], rtstruct_image: Image, roi: ROI,
                                          roi_number: int) -> Tuple[sitk.Image, sitk.Image]:
        self.generate_binary_mask_and_3d_image_called_with_parameters.append(
            {
                'image_slices': image_slices,
                'rtstruct_image': rtstruct_image,
                'roi': roi,
                'roi_number': roi_number
            }
        )
        return self.generate_binary_mask_and_3d_image_return_value

    def get_generate_binary_mask_and_3d_image_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.generate_binary_mask_and_3d_image_called_with_parameters

    def set_generate_binary_mask_and_3d_image_return_value(self, return_value: Any):
        self.generate_binary_mask_and_3d_image_return_value = return_value
