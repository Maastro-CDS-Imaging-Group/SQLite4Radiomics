"""
This module is used to represent a MRISeries object from the DICOMSeries table in the database.
Inherits SeriesWithImageSlices module.
"""
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class MriSeries(SeriesWithImageSlices):
    """
    This class stores all information about a MRI-series from the DICOMSeries table in the database.
    """
    pass
