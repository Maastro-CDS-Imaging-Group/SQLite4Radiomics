"""
This module is used to represent a RadiomicCalculation object from the DICOMRadiomicCalculation table in the database.
"""

import datetime
from typing import List

from logic.entities.patient import Patient
from logic.entities.radiomic_feature_value import RadiomicFeatureValue
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class RadiomicCalculation:
    """
    This class stores all information about a radiomic calculation from the DICOMRadiomicCalculation table in the
    database.
    """

    def __init__(self, patient: Patient, rtstruct_series: RtstructSeries,
                 series_with_image_slices: SeriesWithImageSlices, time: datetime.datetime,
                 identity: int = -1, result: List[RadiomicFeatureValue] = None):
        """
        The constructor of the RadiomicCalculation class.
        :param patient: The patient of the radiomic calculation.
        :param rtstruct_series: The RTSTRUCT-series of the radiomic calculation.
        :param series_with_image_slices: The series with image slices of the radiomic calculation.
        :param time: The time of the radiomic calculation.
        :param identity: The identity of the radiomic calculation.
        :param result: The result of the radiomic calculation.
        """

        # All fields that are used for storing the properties of the radiomic calculation.
        self._identity: int = identity
        self._patient: Patient = patient
        self._rtstruct_series: RtstructSeries = rtstruct_series
        self._series_with_image_slices: SeriesWithImageSlices = series_with_image_slices
        self._time: datetime.datetime = time
        self._result: List[RadiomicFeatureValue] = result

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
            # The method contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._identity: int = value

    @property
    def patient(self) -> Patient:
        """
        The get method of the patient property.
        :return: The value of the _patient field.
        """
        return self._patient

    @patient.setter
    def patient(self, value: Patient) -> None:
        """
        The set method of the patient property.
        :param value: The new value for the patient property.
        :return: The method doesn't return anything.
        """

        # Check whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._patient: Patient = value

    @property
    def rtstruct_series(self) -> RtstructSeries:
        """
        The get method of the rtstruct_series property.
        :return: The value of the _rtstruct_series field.
        """
        return self._rtstruct_series

    @rtstruct_series.setter
    def rtstruct_series(self, value: RtstructSeries) -> None:
        """
        The set method of the rtstruct_series property.
        :param value: The new value for the rtstruct_series property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._rtstruct_series: RtstructSeries = value

    @property
    def series_with_image_slices(self) -> SeriesWithImageSlices:
        """
        The get method of the series_with_image_slices property.
        :return: The value of the _series_with_image_slices field.
        """
        return self._series_with_image_slices

    @series_with_image_slices.setter
    def series_with_image_slices(self, value: SeriesWithImageSlices) -> None:
        """
        The set method for the series_with_image_slices property.
        :param value: The new value for the series_with_image_slices_property.
        :return: THe method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._series_with_image_slices: SeriesWithImageSlices = value

    @property
    def time(self) -> datetime.datetime:
        """
        The get method of the time property.
        :return: The value of the _time field.
        """
        return self._time

    @time.setter
    def time(self, value: datetime.datetime) -> None:
        """
        The set method of the time property.
        :param value: The new value for the time property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._time: datetime.datetime = value

    @property
    def result(self) -> List[RadiomicFeatureValue]:
        """
        The get method of the result property.
        :return: The value of the _result field.
        """
        return self._result

    @result.setter
    def result(self, value: List[RadiomicFeatureValue]) -> None:
        """
        The set method of the result property.
        :param value: The new value for the result property.
        :return: The method doesn't return anything.
        """

        # Checks whether value contains valid data.
        if value is False:
            # The value contains invalid data and so the value of the property won't change.
            return
        # The property is set to it's new value.
        self._result: List[RadiomicFeatureValue] = value
