from typing import List, Optional, Any, Dict

from logic.entities.series import Series
from logic.entities.study import Study


class StudyMockUp(Study):

    def __init__(self, instance: str, date: str, time: str, identity: str, description: str, accession_n: str,
                 refer_physicist: str, patient_ag: str, patients_we: str, modalities: str,
                 series: List[Series] = None) -> None:
        super().__init__(instance, date, time, identity, description, accession_n, refer_physicist, patient_ag,
                         patients_we, modalities, series)

        self.get_instance_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_instance_return_value: Any = None

        self.set_instance_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_instance_return_value: Any = None

        self.get_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_date_return_value: Any = None

        self.set_date_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_date_return_value: Any = None

        self.get_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_time_return_value: Any = None

        self.set_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_time_return_value: Any = None

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_identity_return_value: Any = None

        self.get_description_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_description_return_value: Any = None

        self.set_description_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_description_return_value: Any = None

        self.get_accession_n_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_accession_n_return_value: Any = None

        self.set_accession_n_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_accession_n_return_value: Any = None

        self.get_refer_physicist_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_refer_physicist_return_value: Any = None

        self.set_refer_physicist_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_refer_physicist_return_value: Any = None

        self.get_patients_ag_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_patients_ag_return_value: Any = None

        self.set_patients_ag_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_patients_ag_return_value: Any = None

        self.get_patients_we_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_patients_we_return_value: Any = None

        self.set_patients_we_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_patients_we_return_value: Any = None

        self.get_modalities_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_modalities_return_value: Any = None

        self.set_modalities_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_modalities_return_value: Any = None

        self.get_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_series_return_value: Any = None

        self.set_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_series_return_value: Any = None

        self.add_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.add_series_return_value: Any = None

        self.remove_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.remove_series_return_value: Any = None

    @property
    def instance(self) -> str:
        self.get_instance_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_instance_return_value

    @instance.setter
    def instance(self, value: str) -> None:
        self.set_instance_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def date(self) -> str:
        self.get_date_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_time_return_value

    @date.setter
    def date(self, value: str) -> None:
        self.set_date_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def time(self) -> str:
        self.get_time_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_time_return_value

    @time.setter
    def time(self, value: str) -> None:
        self.set_time_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def identity(self) -> str:
        self.get_identity_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_identity_return_value

    @identity.setter
    def identity(self, value: str) -> None:
        self.set_identity_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def description(self) -> str:
        self.get_description_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_description_return_value

    @description.setter
    def description(self, value: str) -> None:
        self.set_description_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def accession_n(self) -> None:
        self.get_accession_n_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_accession_n_return_value

    @accession_n.setter
    def accession_n(self, value: str) -> None:
        self.set_accession_n_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def refer_physicist(self) -> str:
        self.get_refer_physicist_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_refer_physicist_return_value

    @refer_physicist.setter
    def refer_physicist(self, value: str) -> None:
        self.set_refer_physicist_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def patients_ag(self) -> str:
        self.get_patients_ag_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_patients_ag_return_value

    @patients_ag.setter
    def patients_ag(self, value: str) -> None:
        self.set_patients_ag_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def patients_we(self) -> str:
        self.get_patients_we_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_patients_we_return_value

    @patients_we.setter
    def patients_we(self, value: str) -> None:
        self.set_patients_we_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def modalities(self) -> str:
        self.get_modalities_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_modalities_return_value

    @modalities.setter
    def modalities(self, value: str) -> None:
        self.set_modalities_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def series(self) -> List[Series]:
        self.get_series_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_series_return_value

    @series.setter
    def series(self, value: List[Series]) -> None:
        self.set_series_called_with_parameters.append(
            {
                'value': value
            }
        )

    def add_series(self, series: Series) -> None:
        self.add_series_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.add_series_return_value

    def remove_series(self, series: Series) -> None:
        self.remove_series_called_with_parameters.append(
            {
                'series': series
            }
        )
        return self.remove_series_return_value

    def get_get_instance_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_instance_called_with_parameters

    def set_get_instance_return_value(self, return_value: Any) -> None:
        self.get_instance_return_value = return_value

    def get_set_instance_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_instance_called_with_parameters

    def set_set_instance_return_value(self, return_value: Any) -> None:
        self.set_instance_return_value = return_value

    def get_get_date_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_date_called_with_parameters

    def set_get_date_return_value(self, return_value: Any) -> None:
        self.get_date_return_value = return_value

    def get_set_date_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_date_called_with_parameters

    def set_set_date_return_value(self, return_value: Any) -> None:
        self.set_date_return_value = return_value

    def get_get_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_time_called_with_parameters

    def set_get_time_return_value(self, return_value: Any) -> None:
        self.get_time_return_value = return_value

    def get_set_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_time_called_with_parameters

    def set_set_time_return_value(self, return_value: Any) -> None:
        self.set_time_return_value = return_value

    def get_get_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_identity_called_with_parameters

    def set_get_identity_return_value(self, return_value: Any) -> None:
        self.get_identity_return_value = return_value

    def get_set_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_identity_called_with_parameters

    def set_set_identity_return_value(self, return_value: Any) -> None:
        self.set_identity_return_value = return_value

    def get_get_description_called_with_parameters(self) -> List[Dict[ Optional[str], Any]]:
        return self.get_description_called_with_parameters

    def set_get_description_return_value(self, return_value: Any) -> None:
        self.get_description_return_value = return_value

    def get_set_description_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_description_called_with_parameters

    def set_set_description_return_value(self, return_value: Any) -> None:
        self.get_description_return_value = return_value

    def get_get_accession_n_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_accession_n_called_with_parameters

    def set_get_accession_n_return_value(self, return_value: Any) -> None:
        self.get_accession_n_return_value = return_value

    def get_set_accession_n_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_accession_n_called_with_parameters

    def set_set_accession_n_return_value(self, return_value: Any) -> None:
        self.set_accession_n_return_value = return_value

    def get_get_refer_physicist_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_refer_physicist_called_with_parameters

    def set_get_refer_physicist_return_value(self, return_value: Any) -> None:
        self.get_refer_physicist_return_value = return_value

    def get_set_refer_physicist_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_refer_physicist_called_with_parameters

    def set_set_refer_physicist_return_value(self, return_value: Any) -> None:
        self.set_refer_physicist_return_value = return_value

    def get_get_patients_ag_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_patients_ag_called_with_parameters

    def set_get_patients_ag_return_value(self, return_value: Any) -> None:
        self.get_patients_ag_return_value = return_value

    def get_set_patients_ag_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_patients_ag_called_with_parameters

    def set_set_patients_ag_return_value(self, return_value: Any) -> None:
        self.set_patients_ag_return_value = return_value

    def get_get_patients_we_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return  self.get_patients_we_called_with_parameters

    def set_get_patients_we_return_value(self, return_value: Any) -> None:
        self.get_patients_we_return_value = return_value

    def get_set_patients_we_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_patients_we_called_with_parameters

    def set_set_patients_we_return_value(self, return_value: Any) -> None:
        self.set_patients_we_return_value = return_value

    def get_get_modalities_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_modalities_called_with_parameters

    def set_get_modalities_return_value(self, return_value: Any) -> None:
        self.get_modalities_return_value = return_value

    def get_set_modalities_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_modalities_called_with_parameters

    def set_set_modalities_return_value(self, return_value: Any) -> None:
        self.set_modalities_return_value = return_value

    def get_get_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_series_called_with_parameters

    def set_get_series_return_value(self, return_value: Any) -> None:
        self.get_series_return_value = return_value

    def get_set_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_series_called_with_parameters

    def set_set_series_return_value(self, return_value: Any) -> None:
        self.set_series_return_value = return_value

    def get_add_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.add_series_called_with_parameters

    def set_add_series_return_value(self, return_value: Any) -> None:
        self.add_series_return_value = return_value

    def get_remove_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.remove_series_called_with_parameters

    def set_remove_series_return_value(self, return_value: Any) -> None:
        self.remove_series_return_value = return_value
