"""
This module is used to represent a CTSeries object from the DICOMSeries table in the database.
Inherits SeriesWithImageSlices module.
"""
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class CtSeries(SeriesWithImageSlices):
    """
    This class stores all information about a CT-series from the DICOMSeries table in the database.
    """
    pass
