"""
This module is used to represent a Patient object from the DICOMPatient table in the database.
"""

from typing import List

from logic.entities.study import Study


class Patient:
    """
    The class stores all information about a patient from the DICOMPatient table in the database.
    """

    def __init__(self, identity: str, name: str, sex: str, access_time: str, studies: List[Study] = None):
        """
        The constructor of the Patient class.
        :param identity: The identity of the patient.
        :param name: The name of the patient.
        :param sex: The sex of the patient.
        :param access_time: The access_time of the patient.
        :param studies: The studies of the patient.
        """

        # All fields that are used for storing the properties of the patient.
        self._identity: str = identity
        self._name: str = name
        self._sex: str = sex
        self._access_time: str = access_time

        # Checks whether studies are passed as an argument.
        if studies is None:
            # If no studies are passed, studies equals an empty list.
            studies: List[Study] = []
        # The _studies field is set to it's value.
        self._studies: List[Study] = studies

    @property
    def identity(self) -> str:
        """
        The get method of the identity property.
        :return: The value of the _identity field.
        """
        return self._identity

    @identity.setter
    def identity(self, value: str) -> None:
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
        self._identity: str = value

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
    def sex(self) -> str:
        """
        The get method for the sex property.
        :return: The value for the _sex property.
        """
        return self._sex

    @sex.setter
    def sex(self, value: str) -> None:
        """
        The set method for the sex property.
        :param value: The new value for the sex property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._sex: str = value

    @property
    def access_time(self) -> str:
        """
        The get method of the access_time property.
        :return: The value of the _access_time field.
        """
        return self._access_time

    @access_time.setter
    def access_time(self, value: str) -> None:
        """
        The set method of the access_time property.
        :param value: The new value for the access_time property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._access_time: str = value

    @property
    def studies(self) -> List[Study]:
        """
        The get method of the studies property.
        :return: The value of the _studies field.
        """
        return self._studies

    @studies.setter
    def studies(self, value: List[Study]) -> None:
        """
        The set method of the studies property.
        :param value: The new value for the studies priority.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._studies: List[Study] = value

    def add_study(self, study: Study) -> None:
        """
        Adds study to the studies property.
        :param study: The study to add.
        :return: The method doesn't return anything.
        """

        # Adds study to studies property.
        self._studies.append(study)

    def remove_study(self, study: Study) -> None:
        """
        Removes study from the studies property.
        :param study: The study to remove.
        :return: The method doesn't return anything.
        """

        # Removes study from the studies property.
        self._studies.remove(study)

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare to.
        :return: Returns true if objects are equal and false if they aren't equal.
        """

        # Checks whether other object is instance Patient.
        if not isinstance(other, Patient):
            return False

        # Checks whether fields are equal.
        if self.identity != other.identity:
            return False
        if self.name != other.name:
            return False
        if self.sex != other.sex:
            return False
        return self.access_time == other.access_time

    def __hash__(self) -> int:
        """
        Calculates hash value for the object.
        Overrides the __hash__ method from the object class.
        :return: Hash value of the object.
        """
        return hash((self.identity, self.name))
