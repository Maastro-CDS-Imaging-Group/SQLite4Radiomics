"""
This module is used to represent a RadiomicFeatureValue object from the DICOMRadiomicFeatureValue table from the
database.
"""

from logic.entities.radiomic_class import RadiomicClass
from logic.entities.radiomic_feature import RadiomicFeature
from logic.entities.radiomic_filter import RadiomicFilter
from logic.entities.roi import ROI


class RadiomicFeatureValue:
    """
    This class stores all information about a feature value from the DICOMRadiomicFeatureValue table from the database.
    """

    def __init__(self, roi: ROI, radiomic_filter: RadiomicFilter, radiomic_class: RadiomicClass,
                 feature: RadiomicFeature, value: str):
        """
        The constructor of the RadiomicFeatureValue class.
        :param roi: The region of interest of the feature value.
        :param radiomic_filter: The filter of the feature value.
        :param radiomic_class: The class of the feature value.
        :param feature: The feature of the feature value.
        :param value: The value of the feature value.
        """

        # All fields that are used for storing the properties of the feature value.
        self._roi: ROI = roi
        self._filter: RadiomicFilter = radiomic_filter
        self._radiomic_class: RadiomicClass = radiomic_class
        self._feature: RadiomicFeature = feature
        self._value: str = value

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
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._roi: ROI = value

    @property
    def radiomic_filter(self) -> RadiomicFilter:
        """
        The get method of the radiomic_filter property.
        :return: The value of the _radiomic_filter field.
        """
        return self._filter

    @radiomic_filter.setter
    def radiomic_filter(self, value: RadiomicFilter) -> None:
        """
        The set method of the radiomic_filter property.
        :param value: The new value for the radiomic_filter property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._filter: RadiomicFilter = value

    @property
    def radiomic_class(self) -> RadiomicClass:
        """
        The get method of the radiomic_class property
        :return: The value of the _radiomic_class property.
        """
        return self._radiomic_class

    @radiomic_class.setter
    def radiomic_class(self, value: RadiomicClass):
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
    def feature(self) -> RadiomicFeature:
        """
        The get method of the feature property.
        :return: The value of the _feature field.
        """
        return self._feature

    @feature.setter
    def feature(self, value: RadiomicFeature) -> None:
        """
        The set method of the feature property.
        :param value: The new value for the feature property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._feature: RadiomicFeature = value

    @property
    def value(self) -> str:
        """
        The get method of the value property.
        :return: The value of the _value field.
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """
        The set method of the value property.
        :param value: The new value for the value property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value for the property won't change.
            return
        # The property is set to it's new value.
        self._value: str = value
