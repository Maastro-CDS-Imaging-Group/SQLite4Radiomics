from typing import List, Optional, Any, Dict

from logic.entities.patient import Patient
from logic.entities.study import Study


class PatientMockUp(Patient):

    def __init__(self, identity: str, name: str, sex: str, access_time: str, studies: List[Study] = None):
        super().__init__(identity, name, sex, access_time, studies)

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str],Any]] = []
        self.set_identity_return_value: Any = None

        self.get_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_name_return_value: Any = None

        self.set_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_name_return_value: Any = None

        self.get_sex_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_sex_return_value: Any = None

        self.set_sex_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_sex_return_value: Any = None

        self.get_access_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_access_time_return_value: Any = None

        self.set_access_time_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_access_time_return_value: Any = None

        self.get_studies_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_studies_return_value: Any = None

        self.set_studies_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_studies_return_value: Any = None

        self.add_study_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.add_study_return_value: Any = None

        self.remove_study_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.remove_study_return_value: Any = None

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
        self.get_identity_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def name(self) -> str:
        self.get_name_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_name_return_value

    @name.setter
    def name(self, value: str) -> None:
        self.set_name_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def sex(self) -> str:
        self.get_sex_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_sex_return_value

    @sex.setter
    def sex(self, value: str) -> None:
        self.set_sex_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def access_time(self) -> str:
        self.get_access_time_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_access_time_return_value

    @access_time.setter
    def access_time(self, value: str) -> None:
        self.set_access_time_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def studies(self) -> List[Study]:
        self.get_studies_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_studies_return_value

    @studies.setter
    def studies(self, value: List[Study]) -> None:
        self.set_studies_called_with_parameters.append(
            {
                'value': value
            }
        )

    def add_study(self, study: Study) -> None:
        self.add_study_called_with_parameters.append(
            {
                'study': study
            }
        )
        return self.add_study_return_value

    def remove_study(self, study: Study) -> None:
        self.remove_study_called_with_parameters.append(
            {
                'study': study
            }
        )
        return self.remove_study_return_value

    def get_get_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_identity_called_with_parameters

    def set_get_identity_return_value(self, return_value: Any) -> None:
        self.get_identity_return_value = return_value

    def get_set_identity_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_identity_called_with_parameters

    def set_set_identity_return_value(self, return_value: Any) -> None:
        self.set_identity_return_value = return_value

    def get_get_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_name_called_with_parameters

    def set_get_name_return_value(self, return_value: Any) -> None:
        self.get_name_return_value = return_value

    def get_set_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_name_called_with_parameters

    def set_set_name_return_value(self, return_value: Any) -> None:
        self.set_name_return_value = return_value

    def get_get_sex_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_sex_called_with_parameters

    def set_get_sex_return_value(self, return_value: Any) -> None:
        self.get_sex_return_value = return_value

    def get_set_sex_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_sex_called_with_parameters

    def set_set_sex_return_value(self, return_value: Any) -> None:
        self.set_sex_return_value = return_value

    def get_get_access_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_access_time_called_with_parameters

    def set_get_access_time_return_value(self, return_value: Any) -> None:
        self.get_access_time_return_value = return_value

    def get_set_access_time_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_access_time_called_with_parameters

    def set_set_access_time_return_value(self, return_value: Any) -> None:
        self.set_access_time_return_value = return_value

    def get_get_studies_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_studies_called_with_parameters

    def set_get_studies_return_value(self, return_value: Any) -> None:
        self.get_studies_return_value = return_value

    def get_set_studies_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_studies_called_with_parameters

    def set_set_studies_return_value(self, return_value: Any) -> None:
        self.set_studies_return_value = return_value

    def get_add_study_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.add_study_called_with_parameters

    def set_add_study_return_value(self, return_value: Any) -> None:
        self.add_study_return_value = return_value

    def get_remove_study_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.remove_study_called_with_parameters

    def set_remove_study_return_value(self, return_value: Any) -> None:
        self.remove_study_return_value = return_value