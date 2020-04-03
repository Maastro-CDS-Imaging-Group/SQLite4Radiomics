"""
This module is used to represent a ROI object from the DICOMROI table in the database.
"""


class ROI:
    """
    This class stores all information about a region of interest from the DICOMROI table in the database.
    """

    def __init__(self, name: str, identity: int = -1, priority: int = -1) -> None:
        """
        The constructor of the ROI class.
        :param name: The name of the region of interest.
        :param identity: The identity of the region of interest.
        :param priority: The priority of the region of interest.
        """

        # All fields that are used for storing the properties of the region of interest.
        self._identity: int = identity
        self._name: str = name
        self._priority: int = priority

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
        :param value: The new value for the identity property.
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

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._name: str = value

    @property
    def priority(self) -> int:
        """
        The get method of the priority property.
        :return: The value of the _priority field.
        """
        return self._priority

    @priority.setter
    def priority(self, value: int):
        """
        The set method of the priority property.
        :param value: The new value for the priority property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._priority: int = value

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare to.
        :return: Returns true if objects are equal and false if they aren't equal.
        """

        # Checks whether other object is instance ROI.
        if not isinstance(other, ROI):
            return False

        # Checks whether fields are equal.
        if self.identity != other.identity:
            return False
        return self.name != other.name

    def __hash__(self) -> int:
        """
        Calculates hash value for the object.
        Overrides the __hash__ method from the object class.
        :return: Hash value of the object.
        """
        return hash((self.identity, self.name))
