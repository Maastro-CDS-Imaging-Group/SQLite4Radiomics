from abc import ABC, abstractmethod
import SimpleITK as sitk


# this class unfortunatelly cannot use @dataclass because of the Python version in venv
class ImageMaskStruct:
    """Structure for storing image and its respective mask for image transformations"""
    def __init__(self, image: sitk.Image, mask: sitk.Image) -> None:
        self.image = image
        self.mask = mask


def perform_image_operation(image: sitk.Image, mask: sitk.Image, **kwargs) -> ImageMaskStruct:
    """handles image or mask tranforms prior to radiomics extraction
    :param image: input Image
    :param mask: input Mask
    :return: transformed image and mask
    """
    mode: str = kwargs.pop("mode", "default")
    
    if mode == "default":
        operation: ImageOperation = DefaultImageOperation(**kwargs)
    elif mode == "add_other_operation_here":
        print("see above how to assign the `operation` object")
    else:
        pass
    transformed_struct = operation.transform(image_mask_struct=ImageMaskStruct(image=image, mask=mask))
    
    return transformed_struct.image, transformed_struct.mask
        


class ImageOperation(ABC):
    """Abstract base class for implementation of Image Operations (e.g. pre-processing)"""
    def __init__(self, **kwargs) -> None:
        self.mode = None

    @abstractmethod
    def transform(self, image_mask_struct: ImageMaskStruct) -> ImageMaskStruct:
        """Abstract method for image or mask transformation
        :param image_mask_struct: input ImageMaskStruct
        :return: transformed ImageMaskStruct
        """
        pass


class DefaultImageOperation(ImageOperation):
    """Test - Passes the original instance into the transformed instance"""
    def __init__(self, **kwargs) -> ImageOperation:
        super().__init__(**kwargs)

    def transform(self, image_mask_struct: ImageMaskStruct) -> ImageMaskStruct:
        return image_mask_struct