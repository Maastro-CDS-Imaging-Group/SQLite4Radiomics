"""
This module is used to represent a SeriesWithImageSlices object from the DICOMSeries table in the database.
Inherits Series module
"""

from abc import ABC
from typing import List, Optional

from logic.entities.image import Image
from logic.entities.series import Series


class SeriesWithImageSlices(ABC, Series):
    """
    This class stores all information about a series with image slices from the DICOMSeries table in the database.
    """
    def __init__(self, identity: str, number: str, modality: str, manufacture: str, model_name: str,
                 patient_position: str, date: str, time: str, description: str, body_part_ex: str, protocol_name: str,
                 institution: str, frame_of_reference: str, images: List[Image] = None) -> None:
        """
        The constructor of the SeriesWithImageSlices class.
        :param identity: The identity of the series.
        :param number: The number of the series.
        :param modality: The modality of the series.
        :param manufacture: The manufacture of the series.
        :param model_name: The model name of the series.
        :param patient_position: The patient position of the series.
        :param date: The data of the series.
        :param time: The time of the series.
        :param description: The description of the series.
        :param body_part_ex: The body part ex of the series.
        :param protocol_name: The protocol name of the series.
        :param institution: The institution of the series.
        :param frame_of_reference: The frame of reference of the series.
        :param images: The images of the series.
        """

        # Call the init method of the base class Series.
        super().__init__(identity, number, modality, manufacture, model_name, patient_position)

        # All fields that are used for storing the properties of the series with image slices.
        self._date: str = date
        self._time: str = time
        self._description: str = description
        self._body_part_ex: str = body_part_ex
        self._protocol_name: str = protocol_name
        self._institution:str = institution
        self._frame_of_reference: str = frame_of_reference

        # Checks whether images are passed as an argument.
        if images is None:
            # If no images are passed, images equals an empty list.
            images: List[Image] = []
        # The _studies field is set to it's value.
        self._images: List[Image] = images

    @property
    def date(self) -> str:
        """
        The get method of the date property.
        :return: The value of the _date field.
        """
        return self._date

    @date.setter
    def date(self, value: str) -> None:
        """
        The set method of the date property.
        :param value: The new value for the date property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._date: str = value

    @property
    def time(self) -> str:
        """
        The get method of the time property.
        :return: The value of the _time field.
        """
        return self._time

    @time.setter
    def time(self, value: str) -> None:
        """
        The set method of the time property.
        :param value: The new value for the time property
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._time: str = value

    @property
    def description(self) -> str:
        """
        The get method of the description property.
        :return: The value of the _description field.
        """
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        """
        The set method of the description property.
        :param value: The new value for the description property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._description: str = value

    @property
    def body_part_ex(self) -> str:
        """
        The get method of the body_part_ex property.
        :return: The value of the _body_part_ex field.
        """
        return self._body_part_ex

    @body_part_ex.setter
    def body_part_ex(self, value: str) -> None:
        """
        The set method of the body_part_ex property.
        :param value: The new value for the body_part_ex property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._body_part_ex: str = value

    @property
    def protocol_name(self) -> str:
        """
        The get method of the protocol_name property.
        :return: The value of the _protocol_name field.
        """
        return self._protocol_name

    @protocol_name.setter
    def protocol_name(self, value: str) -> None:
        """
        The set method of the protocol_name property.
        :param value: The new value of the protocol_name property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._protocol_name: str = value

    @property
    def institution(self) -> str:
        """
        The get method of the institution property.
        :return: The value of the _institution field.
        """
        return self._institution

    @institution.setter
    def institution(self, value: str) -> None:
        """
        The set method of the institution property.
        :param value: The new value for the institution property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._institution: str = value

    @property
    def frame_of_reference(self) -> str:
        """
        The get method of the frame_of_reference property.
        :return: The value of the _frame_of_reference field.
        """
        return self._frame_of_reference

    @frame_of_reference.setter
    def frame_of_reference(self, value: str) -> None:
        """
        The set method of the frame_of_reference property.
        :param value: The new value for the frame_of_reference property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._frame_of_reference: str = value

    @property
    def images(self) -> Optional[List[Image]]:
        """
        The get method of the images property.
        :return: The value of the _images field.
        """
        return self._images

    @images.setter
    def images(self, value: List[Image]) -> None:
        """
        The set method of the images property.
        :param value: The new value for the images property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._images: List[Image] = value

    def add_image(self, image: Image) -> None:
        """
        Adds image to the images property.
        :param image: The image to add.
        :return: The method doesn't return anything.
        """

        # Adds image to images property.
        self._images.append(image)

    def remove_image(self, image: Image) -> None:
        """
        Removes image from the images property.
        :param image: The image to remove.
        :return: The method doesn't return anything.
        """

        # Removes image from the images property.
        self.images.remove(image)

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare to.
        :return: Returns true if objects are equal and false if they aren't equal.
        """

        # Checks whether other object is instance SeriesWithImageSlices.
        if not isinstance(other, SeriesWithImageSlices):
            return False

        # Checks whether fields are equal.
        if not super().__eq__(other):
            return False
        if self.date != other.date:
            return False
        if self.time != other.time:
            return False
        if self.description != other.description:
            return False
        if self.body_part_ex != other.body_part_ex:
            return False
        if self.protocol_name != other.protocol_name:
            return False
        if self.institution != other.institution:
            return False
        return self.frame_of_reference == other.frame_of_reference

    def __hash__(self) -> int:
        """
        Calculates hash value for the object.
        Overrides the __hash__ method from the object class.
        :return: Hash value of the object.
        """
        return super().__hash__()
