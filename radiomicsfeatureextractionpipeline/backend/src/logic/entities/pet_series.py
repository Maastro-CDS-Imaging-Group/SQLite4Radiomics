"""
This module is used to represent a PetSeries object from the DICOMSeries table in the database.
Inherits Series module.
"""
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class PetSeries(SeriesWithImageSlices):
    """
    This class stores all information about a PET-series from the DICOMSeries table in the database.
    """
    pass
