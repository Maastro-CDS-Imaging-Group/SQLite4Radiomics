"""
This module is used as a template for all BinaryMaskAnd3DImageGenerators.
All BinaryMaskAnd3DImageGenerators should inherit from this class.
"""
from abc import ABC, abstractmethod
from typing import List, Tuple

import SimpleITK as sitk

from logic.entities.image import Image
from logic.entities.roi import ROI


class BinaryMaskAnd3DImageGenerator(ABC):
    """
    This **Abstract Base Class** is used for generating a binary mask and 3D-image.
    Abstract base class for implementation of the strategy pattern.
    """

    @abstractmethod
    def generate_binary_mask_and_3d_image(self, image_slices: List[Image], rtstruct_image: Image, roi: ROI,
                                          roi_number: int) -> Tuple[sitk.Image, sitk.Image]:
        """
        Generates the binary mask and 3d-image with the given image slices, rtstruct, roi and roi-number.
        :param image_slices: The image slices used to create an 3d-image.
        :param rtstruct_image: The rtstruct that will be used to calculate the binary mask.
        :param roi: The roi that will be used to calculate the binary mask.
        :param roi_number: The number of the roi that will be used to calculate the binary mask.
        :return: The binary mask and the 3d image generated.
        """
        pass
