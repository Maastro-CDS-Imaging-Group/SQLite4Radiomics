"""
This method is used to represent a RadiomicClass object from the DICOMRadiomicClass table in the database.
"""

from logic.entities.radiomic_class import RadiomicClass


class RadiomicFeature:
    """
    This class stores all information about a radiomic class from the DICOMRadiomicClass table in the database.
    """

    def __init__(self, radiomic_class: RadiomicClass, name: str, identity: int = -1):
        """
        The constructor of the RadiomicClass class.
        :param radiomic_class: The parent class of the class.
        :param name: The name of the class.
        :param identity: The identity of the class.
        """

        # All fields that are used for storing the properties of the class.
        self._identity: int = identity
        self._radiomic_class: RadiomicClass = radiomic_class
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
    def radiomic_class(self) -> RadiomicClass:
        """
        The get method of the radiomic_class property.
        :return: The value of the _radiomic_class field.
        """
        return self._radiomic_class

    @radiomic_class.setter
    def radiomic_class(self, value: RadiomicClass) -> None:
        """
        The set method of the radiomic_class property.
        :param value: The new value for the radiomic_class property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._radiomic_class: RadiomicClass = value

    @property
    def name(self) -> str:
        """
        The get method of the name property.
        :return: The value of the _name property.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        The set method of the name property.
        :param value: The new value for the name property.
        :return: The method doesn't return anything.
        """

        # Checks whether value is valid.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is changed to it's new value.
        self._name: str = value
