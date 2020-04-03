import datetime
from typing import List, Optional, Any, Dict

from logic.entities.patient import Patient
from logic.entities.radiomic_calculation import RadiomicCalculation
from logic.entities.radiomic_feature_value import RadiomicFeatureValue
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series_with_image_slices import SeriesWithImageSlices


class RadiomicCalculationMockUp(RadiomicCalculation):

    def __init__(self, patient: Patient, rtstruct_series: RtstructSeries,
                 series_with_image_slices: SeriesWithImageSlices, time: datetime.datetime,
                 identity: int = -1, result: List[RadiomicFeatureValue] = None):
        super().__init__(patient, rtstruct_series, series_with_image_slices, time, identity, result)

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_identity_return_value: Any = None

        self.get_patient_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_patient_return_value: Any = None

        self.set_patient_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_patient_return_value: Any = None

        self.get_rtstruct_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_rtstruct_series_return_value: Any = None

        self.set_rtstruct_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_rtstruct_series_return_value: Any = None

        self.get_series_with_image_slices_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_series_with_image_slices_return_value = None

        self.set_series_with_image_slices_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_series_with_image_slices_return_value: Any = None

        self.get_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_time_return_value: Any = None

        self.set_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_time_return_value: Any = None

        self.get_result_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_result_return_value: Any = None

        self.set_result_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_result_return_value: Any = None

    @property
    def identity(self) -> int:
        self.get_identity_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_identity_return_value

    @identity.setter
    def identity(self, value: int) -> None:
        self.set_identity_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def patient(self) -> Patient:
        self.get_patient_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_patient_return_value

    @patient.setter
    def patient(self, value: Patient) -> None:
        self.set_patient_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def rtstruct_series(self) -> RtstructSeries:
        self.get_rtstruct_series_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_rtstruct_series_return_value

    @rtstruct_series.setter
    def rtstruct_series(self, value: RtstructSeries) -> None:
        self.set_rtstruct_series_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def series_with_image_slices(self) -> SeriesWithImageSlices:
        self.get_series_with_image_slices_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_series_with_image_slices_return_value

    @series_with_image_slices.setter
    def series_with_image_slices(self, value: SeriesWithImageSlices) -> None:
        self.set_series_with_image_slices_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def time(self) -> datetime.datetime:
        self.get_time_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_time_return_value

    @time.setter
    def time(self, value: datetime.datetime) -> None:
        self.set_time_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def result(self) -> List[RadiomicFeatureValue]:
        self.get_result_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_result_return_value

    @result.setter
    def result(self, value: List[RadiomicFeatureValue]) -> None:
        self.set_result_called_with_parameters.append(
            {
                'value': value
            }
        )

    def get_get_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_identity_called_with_parameters

    def set_get_identity_return_value(self, return_value: Any) -> None:
        self.get_identity_return_value = return_value

    def get_set_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_identity_called_with_parameters

    def set_set_identity_return_value(self, return_value: Any) -> None:
        self.set_identity_return_value = return_value

    def get_get_patient_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_patient_called_with_parameters

    def set_get_patient_return_value(self, return_value: Any) -> None:
        self.get_patient_return_value = return_value

    def get_set_patient_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_patient_called_with_parameters

    def set_set_patient_return_value(self, return_value: Any) -> None:
        self.set_patient_return_value = return_value

    def get_get_rtstruct_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_rtstruct_series_called_with_parameters

    def set_get_rtstruct_series_return_value(self, return_value: Any) -> None:
        self.get_rtstruct_series_return_value = return_value

    def get_set_rtstruct_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_rtstruct_series_called_with_parameters

    def set_set_rtstruct_series_return_value(self, return_value: str) -> None:
        self.set_rtstruct_series_return_value = return_value

    def get_get_series_with_image_slices_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_series_with_image_slices_called_with_parameters

    def set_get_series_with_image_slices_return_value(self, return_value: Any) -> None:
        self.get_series_with_image_slices_return_value = return_value

    def get_set_series_with_image_slices_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_series_with_image_slices_called_with_parameters

    def set_set_series_with_image_slices_return_value(self, return_value: Any) -> None:
        self.set_series_with_image_slices_return_value = return_value

    def get_get_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_time_called_with_parameters

    def set_get_time_return_value(self, return_value: Any):
        self.get_time_return_value = return_value

    def get_set_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_time_called_with_parameters

    def set_set_time_return_value(self, return_value: str) -> None:
        self.set_time_return_value = return_value

    def get_get_result_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_result_called_with_parameters

    def set_get_result_return_value(self, return_value: Any) -> None:
        self.get_result_return_value = return_value

    def get_set_result_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_result_called_with_parameters

    def set_set_result_return_value(self, return_value) -> None:
        self.set_result_return_value = return_value
