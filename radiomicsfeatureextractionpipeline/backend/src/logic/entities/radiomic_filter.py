"""
This module is used to represent a RadiomicFilter object from the DICOMRadiomicFilter table in the database.
"""


class RadiomicFilter:
    """
    This class stores all information about a radiomic filter from the DICOMRadiomicFilter table in the database.
    """

    def __init__(self, name: str, identity: int = -1) -> None:
        """
        The constructor of the RadiomicFilter class.
        :param name: The name of the filter.
        :param identity: The identity of the filter.
        """

        # All fields that are used for storing the properties of the filter.
        self._identity: int = identity
        self._name: str = name

    @property
    def identity(self) -> int:
        """
        The get method of the identity property.
        :return: The value of the _identity field.
        """
        return self._identity

    @identity.setter
    def identity(self, value: int) -> None:
        """
        The set method of the identity property.
        :param value: The new value for the identity field.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._identity: int = value

    @property
    def name(self) -> str:
        """
        The get method of the name property.
        :return: The value of the _name field.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        The set method of the name property.
        :param value: The new value for the name property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid input.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is send to it's new value.
        self._name: str = value
