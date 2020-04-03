"""
This module is used to represent a Series object from the DICOMSeries table in the database.
"""

class Series:
    """
    This class stores all information about a series from the DICOMSeries table in the database.
    """
    def __init__(self, identity: str, number: str, modality: str, manufacture: str, model_name: str,
                 patient_position: str):
        """
        The constructor of the Series class.
        :param identity: The identity of the series.
        :param number: The number of the series.
        :param modality: The modality of the series.
        :param manufacture: The manufacture of the series.
        :param model_name: The model name of the series.
        :param patient_position: The patient position of the patient.
        """

        # All fields that are used for storing the properties of the series.
        self._identity: str = identity
        self._number: str = number
        self._modality: str = modality
        self._manufacture: str = manufacture
        self._model_name: str = model_name
        self._patient_position: str = patient_position

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
    def number(self) -> str:
        """
        The get method of the number property.
        :return: The value of the _number field.
        """
        return self._number

    @number.setter
    def number(self, value: str) -> None:
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
        self._number: str = value

    @property
    def modality(self) -> str:
        """
        The get method of the modality property.
        :return: The value of the _modality field.
        """
        return self._modality

    @modality.setter
    def modality(self, value: str) -> None:
        """
        The set method of the modality property.
        :param value: The new value for the modality property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._modality: str = value

    @property
    def manufacture(self) -> str:
        """
        The get method of the manufacture property.
        :return: The value of the _manufacture field.
        """
        return self._manufacture

    @manufacture.setter
    def manufacture(self, value: str) -> None:
        """
        The set method of the manufacture property.
        :param value: The new value for the manufacture property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._manufacture: str = value

    @property
    def model_name(self) -> str:
        """
        The get method of the model_name property.
        :return: The value of the _model_name field.
        """
        return self.model_name

    @model_name.setter
    def model_name(self, value: str) -> None:
        """
        The set method of the model_name property.
        :param value: The new value for the model_name property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._model_name: str = value

    @property
    def patient_position(self) -> str:
        """
        The get method of the patient_position property.
        :return: The value of the _patient_position field.
        """
        return self._patient_position

    @patient_position.setter
    def patient_position(self, value: str) -> None:
        """
        The set method of the patient_position property.
        :param value: The new value for the patient_position property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._patient_position: str = value

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare.
        :return: Returns true if objects are equal and false if true aren't equal.
        """

        # Checks whether other object is instance Series.
        if not isinstance(other, Series):
            return False

        # Checks whether fields are equal.
        if self.identity != other.identity:
            return False
        if self.number != other.number:
            return False
        if self.modality != other.modality:
            return False
        if self.manufacture != other.manufacture:
            return False
        return self.patient_position == other.patient_position

    def __hash__(self) -> int:
        """
        Calculates hash value for the object.
        Overrides the __hash__ method from the object class.
        :return: Hash value of the object.
        """
        return hash((self.identity, self.modality))
