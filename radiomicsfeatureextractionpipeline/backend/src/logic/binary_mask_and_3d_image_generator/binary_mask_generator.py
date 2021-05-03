import os
from typing import List, Tuple, Optional, Any

import SimpleITK as sitk
import numpy as np
import pydicom
from skimage import draw

from logic.binary_mask_and_3d_image_generator.binary_mask_and_3d_image_generator import \
    BinaryMaskAnd3DImageGenerator
from logic.entities.image import Image
from logic.entities.roi import ROI


class BinaryMaskGenerator(BinaryMaskAnd3DImageGenerator):

    def generate_binary_mask_and_3d_image(self, image_slices: List[Image], rtstruct_image: Image, roi: ROI,
                                          roi_number: int):
        return self.image_pre_processing(image_slices, rtstruct_image, roi_number)

    def image_pre_processing(self, images_slices: List[Image], rtstruct_image: Image, roi_number: int,
                             npat: str = '', convert: bool = False, export_directory: str = '') -> Tuple[sitk.Image,
                                                                                                         sitk.Image]:
        # list(map(lambda p: print(len(p)), ct_image[0].pixel_array))
        content_first_image: pydicom.FileDataset = images_slices[0].content
        IM_P: np.ndarray = self.get_pixels(images_slices)
        content_rtstruct: pydicom.FileDataset = rtstruct_image.content
        number_of_slices: int = len(images_slices)

        mask: np.ndarray = np.zeros([number_of_slices, content_first_image.Rows, content_first_image.Columns],
                                    dtype=np.uint8)
        resolution_x: np.ndarray = np.array(content_first_image.PixelSpacing[0])
        resolution_y: np.ndarray = np.array(content_first_image.PixelSpacing[1])
        resolution_z: np.ndarray = np.abs(
            images_slices[2].content.ImagePositionPatient[2] - images_slices[3].content.ImagePositionPatient[2])
        try:
            origin: Tuple[float, float, float] = content_first_image.GetOrigin()
        except:
            origin: Tuple[float, float, float] = (0.0, 0.0, 0.0)

        # print("The ROI is", roi_name, "\nROI_id is", roi_number)
        if content_first_image.Modality == 'MR' or 'CT' or 'PT':
            mask: Optional[np.ndarray] = self.image_pre_processing_ct_mri_and_pet(
                content_rtstruct, roi_number, number_of_slices, images_slices, content_first_image, resolution_x,
                resolution_y, IM_P, mask)
        else:
            mask: Optional[np.ndarray] = self.image_pre_processing_mri()
        # print("Image shape is", IM_P.astype(np.float32).shape,
        #   "\nMask shape is", mask.shape)

        # convert image_array to image
        img: sitk.Image = sitk.GetImageFromArray(IM_P.astype(np.float32))
        mask: sitk.Image = sitk.GetImageFromArray(mask)
        # print('Image spacing',mask.GetSpacing())
        img.SetSpacing((float(resolution_x), float(resolution_y), float(resolution_z)))
        mask.SetSpacing((float(resolution_x), float(resolution_y), float(resolution_z)))
        img.SetOrigin(origin)
        mask.SetOrigin(origin)

        if convert:
            if not os.path.exists(export_directory + '/converted_nrrds'):
                os.makedirs(export_directory + '/converted_nrrds')
            if not os.path.exists(export_directory + '/converted_nrrds/' + npat):
                os.makedirs(export_directory + '/converted_nrrds/' + npat)

            export_directory: str = os.path.join(export_directory, 'converted_nrrds', npat)
            image_file_name: str = 'image.nrrd'
            mask_file_name: str = 'mask.nrrd'
            sitk.WriteImage(img, os.path.join(export_directory, image_file_name))  # save image and binary mask locally
            sitk.WriteImage(mask, os.path.join(export_directory, mask_file_name))

        return img, mask

    def image_pre_processing_ct_mri_and_pet(self, content_first_image: pydicom.FileDataset, roi_number: int, num_slice: int,
                                        image_slices: List[Image], content_rtstruct: pydicom.FileDataset,
                                        resolution_x: np.ndarray, resolution_y: np.ndarray, IM_P: np.ndarray,
                                        mask: np.ndarray) -> Optional[np.ndarray]:
        roi_contour_sequence_index: int = -1

        index: int
        roi_contour_sequence: pydicom.FileDataset
        for index, roi_contour_sequence in enumerate(content_first_image.ROIContourSequence):
            if roi_contour_sequence.ReferencedROINumber != roi_number:
                continue
            roi_contour_sequence_index: int = index
            break

        if roi_contour_sequence_index == -1:
            return

        k: int
        for k in range(len(content_first_image.ROIContourSequence[roi_contour_sequence_index].ContourSequence)):
            c_position_rt: np.ndarray = content_first_image.ROIContourSequence[
                roi_contour_sequence_index].ContourSequence[k].ContourData[2]

            # generate a vector of ImagePositionPatient[2]
            # usage get_image_position_patient(index, img_vol)
            get_image_position_patient: Any = lambda pos_x, pos_y: pos_y[pos_x].content.ImagePositionPatient[2]
            list_get_ipp: np.ndarray = np.zeros((num_slice,))

            i: int
            for i in range(num_slice):  # ?? map()
                list_get_ipp[i]: np.ndarray = get_image_position_patient(i, image_slices)
            slice_ok: np.ndarray = np.argmin(np.abs(c_position_rt - list_get_ipp))

            '''
            for i in range(num_slice):
                if np.abs(c_position_rt - img_vol[i].ImagePositionPatient[2])<0.001:
                 # match the binary mask and the corresponding slice
                    slice_ok = i
                    break
            '''
            x: List[int] = []
            y: List[int] = []
            z: List[int] = []

            m: np.ndarray = content_first_image.ROIContourSequence[
                roi_contour_sequence_index].ContourSequence[k].ContourData

            i: int
            for i in range(0, len(m), 3):
                x.append(m[i + 1])
                y.append(m[i + 0])
                z.append(m[i + 2])
            x: np.ndarray = np.array(x)
            y: np.ndarray = np.array(y)
            z: np.ndarray = np.array(z)
            # print('point-2')
            x -= content_rtstruct.ImagePositionPatient[1]
            y -= content_rtstruct.ImagePositionPatient[0]
            z -= content_rtstruct.ImagePositionPatient[2]
            pts: np.ndarray = np.zeros([len(x), 3])
            pts[:, 0] = x
            pts[:, 1] = y
            pts[:, 2] = z
            a: int = 0
            b: int = 1
            m = np.zeros([2, 2])
            m[0, 0]: np.ndarray = image_slices[slice_ok].content.ImageOrientationPatient[a] * resolution_x
            m[0, 1]: np.ndarray = image_slices[slice_ok].content.ImageOrientationPatient[a + 3] * resolution_y
            m[1, 0]: np.ndarray = image_slices[slice_ok].content.ImageOrientationPatient[b] * resolution_x
            m[1, 1]: np.ndarray = image_slices[slice_ok].content.ImageOrientationPatient[b + 3] * resolution_y
            # print('point-3')
            # Transform points from reference frame to image coordinates
            m_inv: np.ndarray = np.linalg.inv(m)
            pts: np.ndarray = (np.matmul(m_inv, (pts[:, [a, b]]).T)).T
            mask[slice_ok, :, :] = np.logical_or(
                mask[slice_ok, :, :],
                self.create_mask_from_rtstruct(pts[:, 0], pts[:, 1], [IM_P.shape[1], IM_P.shape[2]]))
            return mask

    def image_pre_processing_mri(self) -> Optional[np.ndarray]:
        pass

    @staticmethod
    def get_pixels(image_slices: List[Image]) -> np.ndarray:
        image: np.ndarray = np.stack([s.content.pixel_array for s in image_slices])
        image: np.ndarray = image.astype(np.int16)
        # the code below checks if the image has slope and intercept
        # since MRI images often do not provide these
        try:
            intercept: int = image_slices[0].content.RescaleIntercept
            slope: int = image_slices[0].content.RescaleSlope
        except AttributeError:
            pass
        else:
            if slope != 1:
                image: np.ndarray = slope * image.astype(np.float64)
                image: np.ndarray = image.astype(np.int16)
            image += np.int16(intercept)
        return np.array(image, dtype=np.int16)

    @staticmethod
    def create_mask_from_rtstruct(vertex_row_coordinates: np.ndarray, vertex_col_coordinates: np.ndarray,
                                  shape: List[int]) -> np.ndarray:

        fill_row_coordinates: np.ndarray
        fill_col_coordinates: np.ndarray
        fill_row_coordinates, fill_col_coordinates = draw.polygon(vertex_row_coordinates, vertex_col_coordinates, shape)
        mask: np.ndarray = np.zeros(shape, dtype=np.bool)
        mask[fill_row_coordinates, fill_col_coordinates]: bool = True
        return mask