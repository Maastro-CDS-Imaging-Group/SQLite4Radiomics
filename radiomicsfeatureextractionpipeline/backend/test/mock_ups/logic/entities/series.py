from typing import Optional, Any, Dict, List

from logic.entities.series import Series


class SeriesMockUp(Series):

    def __init__(self, identity: str, number: str, modality: str, manufacture: str, model_name: str,
                 patient_position:str):
        super().__init__(identity, number, modality, manufacture, model_name, patient_position)

        self.get_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_identity_return_value: Any = None

        self.set_identity_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_identity_return_value: Any = None

        self.get_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_number_return_value: Any = None

        self.set_number_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_number_return_value: Any = None

        self.get_modality_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_modality_return_value: Any = None

        self.set_modality_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_modality_return_value: Any = None

        self.get_manufacture_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_manufacture_return_value: Any = None

        self.set_manufacture_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_manufacture_return_value: Any = None

        self.get_model_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_model_name_return_value: Any = None

        self.set_model_name_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_model_name_return_value: Any = None

        self.get_patient_position_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_patient_position_return_value: Any = None

        self.set_patient_position_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.set_patient_position_return_value: Any = None

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
    def number(self) -> str:
        self.get_number_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_number_return_value

    @number.setter
    def number(self, value: str) -> None:
        self.set_identity_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def modality(self) -> str:
        self.get_modality_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_modality_return_value

    @modality.setter
    def modality(self, value: str) -> None:
        self.set_modality_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def manufacture(self) -> str:
        self.get_manufacture_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_manufacture_return_value

    @manufacture.setter
    def manufacture(self, value: str) -> None:
        self.set_manufacture_called_with_parameters.append(
            {
                'value': value
            }
        )
    
    @property
    def model_name(self) -> str:
        self.get_model_name_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_model_name_return_value
    
    @model_name.setter
    def model_name(self, value: str) -> None:
        self.set_model_name_called_with_parameters.append(
            {
                'value': value
            }
        )

    @property
    def patient_position(self) -> str:
        self.get_patient_position_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_patient_position_return_value

    @patient_position.setter
    def patient_position(self, value: str) -> None:
        self.set_patient_position_called_with_parameters.append(
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

    def get_get_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_number_called_with_parameters

    def set_get_number_return_value(self, return_value: Any) -> None:
        self.get_number_return_value = return_value

    def get_set_number_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_number_called_with_parameters

    def set_set_number_return_value(self, return_value: Any) -> None:
        self.set_number_return_value = return_value

    def get_get_modality_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_modality_called_with_parameters

    def set_get_modality_return_value(self, return_value: Any) -> None:
        self.get_modality_return_value = return_value

    def get_set_modality_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_modality_called_with_parameters

    def set_set_modality_return_value(self, return_value: Any) -> None:
        self.set_modality_return_value = return_value

    def get_get_manufacture_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_manufacture_called_with_parameters

    def set_get_manufacture_return_value(self, return_value: Any) -> None:
        self.get_manufacture_return_value: Any = return_value

    def get_set_manufacture_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_manufacture_called_with_parameters

    def set_set_manufacture_return_value(self, return_value: Any) -> None:
        self.set_manufacture_return_value = return_value

    def get_get_model_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_model_name_called_with_parameters

    def set_get_model_name_return_value(self, return_value: Any) -> None:
        self.get_model_name_return_value = return_value

    def get_set_model_name_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_model_name_called_with_parameters

    def set_set_model_name_return_value(self, return_value: Any) -> None:
        self.get_model_name_return_value = return_value

    def get_get_patient_position_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_patient_position_called_with_parameters

    def set_get_patient_position_return_value(self, return_value: Any) -> None:
        self.get_patient_position_return_value = return_value

    def get_set_patient_position_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.set_patient_position_called_with_parameters

    def set_set_patient_position_return_value(self, return_value: Any) -> None:
        self.set_patient_position_return_value = return_value
