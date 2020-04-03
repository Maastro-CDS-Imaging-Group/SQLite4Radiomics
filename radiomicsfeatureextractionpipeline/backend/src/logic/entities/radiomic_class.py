"""
This module is used to represent a RadiomicClass object from the DICOMRadiomicClass table in the database.
"""

class RadiomicClass:
    """
    This class stores all information about a radiomic class from the DICOMRadiomicClass table in the database.
    """

    def __init__(self, name: str, identity: int = -1, parent_class: 'RadiomicClass' = None):
        """
        The constructor of the RadiomicClass class.
        :param name: The name of the radiomic class.
        :param identity: The identity of the radiomic class.
        :param parent_class: The parent radiomic class of the radiomic class.
        """

        # All fields that are used for storing the properties of the radiomic class.
        self._identity: int = identity
        self._parent_class: RadiomicClass = parent_class
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
        :param value: The new value of the identity property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._identity: int = value

    @property
    def parent_class(self) -> 'RadiomicClass':
        """
        The get method of the parent_class property.
        :return: The value of the _parent_class field.
        """
        return self._parent_class

    @parent_class.setter
    def parent_class(self, value: 'RadiomicClass') -> None:
        """
        The set method of the parent_class property.
        :param value: The new value for the parent_class property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._parent_class: RadiomicClass = value

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
        :param value: The new value for the property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is changed to it's new value.
        self._name: str = value
