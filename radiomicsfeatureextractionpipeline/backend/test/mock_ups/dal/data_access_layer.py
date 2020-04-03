from typing import Optional, Any, Dict, List

from dal.data_access_layer import DataAccessLayer
from dal.image_repository import ImageRepository
from dal.patient_repository import PatientRepository
from dal.radiomic_feature_repository import RadiomicFeatureRepository
from dal.roi_repository import ROIRepository
from dal.series_repository import SeriesRepository
from dal.study_repository import StudyRepository


class DataAccessLayerMockUp(DataAccessLayer):

    def __init__(self, image_repos: ImageRepository, patient_repos: PatientRepository,
                 radiomic_feature_repos: RadiomicFeatureRepository, roi_repos: ROIRepository,
                 series_repos: SeriesRepository, study_repos: StudyRepository):
        super().__init__(image_repos, patient_repos, radiomic_feature_repos, roi_repos, series_repos, study_repos)

        self.get_image_repos_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_image_repos_return_value: Any = None

        self.get_patient_repos_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_patient_repos_return_value: Any = None

        self.get_radiomic_feature_repos_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_radiomic_feature_repos_return_value: Any = None

        self.get_roi_repos_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_roi_repos_return_value: Any = None

        self.get_series_repos_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_series_repos_return_value: Any = None

        self.get_study_repos_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_study_repos_return_value: Any = None

    def get_image_repos(self) -> ImageRepository:
        self.get_image_repos_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_image_repos_return_value

    def get_patient_repos(self) -> PatientRepository:
        self.get_patient_repos_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_patient_repos_return_value

    def get_radiomic_feature_repos(self) -> RadiomicFeatureRepository:
        self.get_radiomic_feature_repos_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_radiomic_feature_repos_return_value

    def get_roi_repos(self) -> ROIRepository:
        self.get_roi_repos_called_with_parameters. append(
            {
                None: None
            }
        )
        return self.get_roi_repos_return_value

    def get_series_repos(self) -> SeriesRepository:
        self.get_series_repos_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_series_repos_return_value

    def get_study_repos(self) -> StudyRepository:
        self.get_study_repos_called_with_parameters.append(
            {
                None: None
            }
        )
        return self.get_study_repos_return_value

    def get_get_image_repos_called_with_parameter(self) -> List[Dict[Optional[str], Any]]:
        return self.get_image_repos_called_with_parameters

    def set_get_image_repos_return_value(self, return_value: Any) -> None:
        self.get_image_repos_return_value = return_value

    def get_get_patient_repos_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_patient_repos_called_with_parameters

    def set_get_patient_repos_return_value(self, return_value: Any) -> None:
        self.get_patient_repos_return_value = return_value

    def get_get_radiomic_feature_repos_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_radiomic_feature_repos_called_with_parameters

    def set_get_radiomic_feature_repos_return_value(self, return_value: Any) -> None:
        self.get_radiomic_feature_repos_return_value = return_value

    def get_get_roi_repos_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_roi_repos_called_with_parameters

    def set_get_roi_repos_return_value(self, return_value: Any) -> None:
        self.get_roi_repos_return_value = return_value

    def get_get_series_repos_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_series_repos_called_with_parameters

    def set_get_series_repos_return_value(self, return_value: Any) -> None:
        self.get_series_repos_return_value = return_value

    def get_get_study_repos_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_study_repos_called_with_parameters

    def set_get_study_repos_return_value(self, return_value: Any) -> None:
        self.get_study_repos_return_value = return_value
