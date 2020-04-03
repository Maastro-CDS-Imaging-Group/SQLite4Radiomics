"""
This module is used to represent a Segmentation object from the DICOMSeriesROI table in the database.
"""

from logic.entities.roi import ROI
from logic.entities.rtstruct_series import RtstructSeries


class Segmentation:
    """
    This class stores all information about a segmentation from the DICOMSeriesROI table in the database.
    """

    def __init__(self, roi: ROI, series: RtstructSeries, number: int, file_path: str) -> None:
        """
        The constructor of the Segmentation class.
        :param roi: The roi of the segmentation.
        :param series: The series of the segmentation.
        :param number: The number of the segmentation.
        :param file_path: The file path of the segmentation.
        """

        # All fields that are used for storing the properties of the segmentation.
        self._roi: ROI = roi
        self._series: RtstructSeries = series
        self._number: int = number
        self._file_path: str = file_path

    @property
    def roi(self) -> ROI:
        """
        The get method of the roi property.
        :return: The value of the _roi field.
        """
        return self._roi

    @roi.setter
    def roi(self, value: ROI) -> None:
        """
        The set method of the roi property.
        :param value: The new value for the roi property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._roi: ROI = value

    @property
    def series(self) -> RtstructSeries:
        """
        The get method of the series property.
        :return: The value of the _series field.
        """
        return self._series

    @series.setter
    def series(self, value: RtstructSeries) -> None:
        """
        The set method of the series property.
        :param value: The new value for the series property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._series: RtstructSeries = value

    @property
    def number(self) -> int:
        """
        The get method of the number property.
        :return: The value of the _number field.
        """
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        """
        The set method of the number property.
        :param value: The new value for the number property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._number: int = value

    @property
    def file_path(self) -> str:
        """
        The get method of the file_path property.
        :return: The value of the _file_path field.
        """
        return self._file_path

    @file_path.setter
    def file_path(self, value: str) -> None:
        """
        The set method of the file_path property.
        :param value: The new value for the file_path property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._file_path: str = value

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare to.
        :return: Returns true if objects are equal and false if they aren't equal.
        """

        # Checks whether other object is instance Segmentation.
        if not isinstance(other, Segmentation):
            return False

        # Checks whether fields are equal.
        if self.roi != other.roi:
            return False
        return self.series == other.roi

    def __hash__(self) -> int:
        """
        Calculates hash value for the object.
        Overrides the __hash__method from the object class.
        :return: Hash value of the object.
        """
        return hash((self.roi, self.series))
