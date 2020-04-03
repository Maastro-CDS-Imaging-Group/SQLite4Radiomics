from typing import List, Optional, Tuple, Any, Dict

from dal.database_connector import DatabaseConnector
from dal.image_repository import ImageRepository
from dal.patient_repository import PatientRepository
from dal.series_repository import SeriesRepository
from dal.study_repository import StudyRepository
from logic.entities.image import Image
from logic.entities.patient import Patient
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.series import Series
from logic.entities.series_with_image_slices import SeriesWithImageSlices
from test.mock_ups.dal.repository import RepositoryMockUp


class ImageRepositoryMockUp(ImageRepository, RepositoryMockUp):

    def __init__(self, database_connector: DatabaseConnector, series_repos: SeriesRepository,
                 patient_repos: PatientRepository, study_repos: StudyRepository, query_directory: str) -> None:
        super().__init__(database_connector, series_repos, patient_repos, study_repos, query_directory)

        self.get_all_images_of_series_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_all_images_of_series_return_value: Any = None

        self.get_image_by_id_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_image_by_id_return_value: Any = None

        self.get_images_of_patients_last_ct_series_matching_rtstruct_called_with_parameters: List[
            Dict[Optional[str], Any]] = []
        self.get_images_of_patients_last_ct_series_matching_rtstruct_return_value: Any = None

        self.get_image_by_file_path_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.get_image_by_file_path_return_value: Any = None

    def get_all_images_of_series(self, series: Series) -> List[Image]:
        self.get_all_images_of_series_called_with_parameters.append(
            {
                'series': series
            }
        )
        return self.get_all_images_of_series_return_value

    def get_image_by_id(self, image_id: str) -> Optional[Image]:
        self.get_image_by_id_called_with_parameters.append(
            {
                'image_id': image_id
            }
        )
        return self.get_image_by_id_return_value

    def get_images_of_patients_last_ct_series_matching_rtstruct(
            self, sop_instance: str) -> List[Tuple[Patient, RtstructSeries, SeriesWithImageSlices]]:
        self.get_images_of_patients_last_ct_series_matching_rtstruct_called_with_parameters.append(
            {
                'sop_instance': sop_instance
            }
        )
        return self.get_images_of_patients_last_ct_series_matching_rtstruct_return_value

    def get_image_by_file_path(self, file_path: str) -> Optional[Image]:
        self.get_image_by_id_called_with_parameters.append(
            {
                'file_path': file_path
            }
        )
        return self.get_image_by_file_path_return_value

    def get_get_images_from_series_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_all_images_of_series_called_with_parameters

    def set_get_images_from_series_return_value(self, return_value: Any) -> None:
        self.get_all_images_of_series_return_value = return_value

    def get_get_image_by_id_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_image_by_id_called_with_parameters

    def set_get_image_by_id_return_value(self, return_value: Any) -> None:
        self.get_image_by_id_return_value = return_value

    def get_get_images_of_patients_last_ct_series_matching_rtstruct_called_with_parameters(self) -> List[
            Dict[Optional[str], Any]]:
        return self.get_images_of_patients_last_ct_series_matching_rtstruct_called_with_parameters

    def set_get_images_of_patients_last_ct_series_matching_rtstruct_return_value(self, return_value: Any) -> None:
        self.get_images_of_patients_last_ct_series_matching_rtstruct_return_value = return_value

    def get_get_image_by_file_path_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.get_image_by_file_path_called_with_parameters

    def set_get_image_by_file_path_return_value(self, return_value: Any) -> None:
        self.get_image_by_file_path_return_value = return_value
