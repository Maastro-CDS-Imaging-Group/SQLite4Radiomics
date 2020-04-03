"""
This module is used to represent a RtstructSeries object from the DICOMSeries table in the database.
Inherits Series module
"""

from logic.entities.image import Image
from logic.entities.series import Series


class RtstructSeries(Series):
    """
    This class stores all information about all RTSTRUCT-series from the DICOMSeries table in the database.
    """

    def __init__(self, identity: str, number: str, modality: str, manufacture: str, model_name: str,
                 patient_position: str, image: Image = None):
        """
        The constructor of the RtstructSeries class.
        :param identity: The identity of the series.
        :param number: The number of the series.
        :param modality: The modality of the series.
        :param manufacture: The manufacture of the series.
        :param model_name: The model name of the series.
        :param patient_position: The patient position of the series.
        :param image: The image of the series.
        """

        # Call the init method of the base class Series.
        super().__init__(identity, number, modality, manufacture, model_name, patient_position)

        # All fields that are used for storing the properties of the RTSTRUCT-series.
        self._image: Image = image

    @property
    def image(self) -> Image:
        """
        The get method of the image property.
        :return: The value of the _image field.
        """
        return self._image

    @image.setter
    def image(self, value: Image) -> None:
        """
        The set method of the image property.
        :param value: The new value of the image property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._image: Image = value

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare to.
        :return: Returns true if objects are equal and false if they aren't equal.
        """

        # Checks whether other object is instance RtstructSeries.
        if not isinstance(other, RtstructSeries):
            return False

        # Checks whether fields are equal.
        return super().__eq__(other)

    def __hash__(self) -> int:
        """
        Calculates hash value for the object.
        Overrides the __hash__ method from the object class.
        :return: Hash value of the object.
        """
        return super().__hash__()
