"""
This module is used to represent a Study object from the DICOMStudies table in the database.
"""

from typing import List

from logic.entities.series import Series


class Study:
    """
    This class stores all information about a study from the DICOMStudies table in the database.
    """

    def __init__(self, instance: str, date: str, time: str, identity: str, description: str, accession_n: str,
                 refer_physicist: str, patients_ag: str, patients_we: str, modalities: str,
                 series: List[Series] = None) -> None:
        """
        The constructor of the Study class.
        :param instance: The instance of the study.
        :param date: The date of the study.
        :param time: The time of the study.
        :param identity: The identity if the study.
        :param description: The description of the study.
        :param accession_n: The accession n of the study.
        :param refer_physicist: The refer physicist of the study.
        :param patients_ag: The patients ag of the study.
        :param patients_we: The patients we of the study.
        :param modalities: The modalities of the study.
        :param series: The series of the study.
        """

        # All fields that are used for storing the properties of the study.
        self._instance: str = instance
        self._date: str = date
        self._time: str = time
        self._identity: str = identity
        self._description: str = description
        self._accession_n: str = accession_n
        self._refer_physicist: str = refer_physicist
        self._patients_ag: str = patients_ag
        self._patients_we: str = patients_we
        self._modalities: str = modalities

        # Checks whether series are passed as an argument.
        if series is None:
            # If no series are passed, series equals an empty list.
            series: List[Series] = []
        # The _series field is set to it's value.
        self._series: List[Series] = series

    @property
    def instance(self) -> str:
        """
        The get method of the instance property.
        :return: The value of the _instance property.
        """
        return self._instance

    @instance.setter
    def instance(self, value: str) -> None:
        """
        The set method of the instance property.
        :param value: The new value for the instance property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's mew value.
        self._instance: str = value

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
        :param value: The new value for the time property.
        :return: The method doesn't return anything.
        """

        # Checks whether the value contains invalid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._time: str = value

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

        # Checks whether the value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._identity: str = value

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

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._description: str = value

    @property
    def accession_n(self) -> str:
        """
        The get method of the accession_n property.
        :return: The value of the _accession_n field.
        """
        return self._accession_n

    @accession_n.setter
    def accession_n(self, value: str) -> None:
        """
        The set method of the accession_n property.
        :param value: The new value for the accession_n property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._accession_n: str = value

    @property
    def refer_physicist(self) -> str:
        """
        The get method of the refer_physicist property.
        :return: The value of the _refer_physicist field.
        """
        return self._refer_physicist

    @refer_physicist.setter
    def refer_physicist(self, value: str) -> None:
        """
        The set method of the refer_physicist property.
        :param value: The new value for the refer_physicist property.
        :return: The method doesn't return anything.
        """

        # Check whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._refer_physicist: str = value

    @property
    def patients_ag(self) -> str:
        """
        The get method of the patients_ag property.
        :return: The value of the _patients_ag field.
        """
        return self._patients_ag

    @patients_ag.setter
    def patients_ag(self, value: str) -> None:
        """
        The set method of the patients_ag property.
        :param value: The new value for the patients_ag property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._patients_ag: str = value

    @property
    def patients_we(self) -> str:
        """
        The get method of the patients_we property.
        :return: The value of the _patients_we field.
        """
        return self._patients_we

    @patients_we.setter
    def patients_we(self, value: str) -> None:
        """
        The set method of the patients_we property.
        :param value: The new value for the patients_we property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._patients_we: str = value

    @property
    def modalities(self) -> str:
        """
        The get method of the modalities property.
        :return: The value of the _modalities field.
        """
        return self._modalities

    @modalities.setter
    def modalities(self, value: str) -> None:
        """
        The set method of the modalities property.
        :param value: The new value for the modalities property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._modalities: str = value

    @property
    def series(self) -> List[Series]:
        """
        The get method for the series property.
        :return: The value for the _series field.
        """
        return self._series

    @series.setter
    def series(self, value: List[Series]) -> None:
        """
        The set method for the series property.
        :param value: The new value for the series property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._series: List[Series] = value

    def add_series(self, series: Series) -> None:
        """
        Adds series to the series property.
        :param series: The series to add.
        :return: The method doesn't return anything.
        """

        # Adds series to series property.
        self._series.append(series)

    def remove_series(self, series: Series) -> None:
        """
        Removes series from the series property.
        :param series: THe series to remove.
        :return: The method doesn't return anything.
        """

        # Removes series from the series property.
        self._series.remove(series)

    def __eq__(self, other: object) -> bool:
        """
        Checks whether object is equal to other object.
        Overrides the __eq__ method from the object class.
        :param other: The object to compare to.
        :return: Returns true if objects are equal and false if they aren't equal.
        """

        # Checks whether other object is instance Study.
        if not isinstance(other, Study):
            return False

        # Checks whether fields are equal.
        if self.instance != other.instance:
            return False
        if self.date != other.date:
            return False
        if self.time != other.time:
            return False
        if self.identity != other.identity:
            return False
        if self.description != other.description:
            return False
        if self.accession_n != other.accession_n:
            return False
        if self.refer_physicist != other.refer_physicist:
            return False
        if self.patients_ag != other.patients_ag:
            return False
        if self.patients_we != other.patients_we:
            return False
        return self.modalities == other.modalities

    def __hash__(self) -> int:
        """
        Calculates hash value of the object.
        Overrides the __hash__ method from the object class.
        :return: Hash value of the object.
        """
        return hash((self.instance, self.date, self.time))
