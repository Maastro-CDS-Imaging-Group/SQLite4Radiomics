from typing import Any, Dict, Optional, List

import SimpleITK as sitk

from dal.radiomic_feature_repository import RadiomicFeatureRepository
from logic.feature_extractor.feature_calculator import FeatureCalculator
from logic.entities.radiomic_calculation import RadiomicCalculation
from logic.entities.roi import ROI


class FeatureCalculatorMockUp(FeatureCalculator):

    def __init__(self, radiomic_feature_repos: RadiomicFeatureRepository, parameter_file: str) -> None:
        super().__init__(radiomic_feature_repos, parameter_file)

        self.calculate_features_called_with_parameters: List[Dict[Optional[str], Any]] = []
        self.calculate_features_return_value: Any = None

    def calculate_features(self, radiomic_calculation: RadiomicCalculation, image: sitk.Image, mask: sitk.Image,
                           roi: ROI) -> None:
        self.calculate_features_called_with_parameters.append(
            {
                'radiomic_calculation': radiomic_calculation,
                'image': image,
                'mask': mask,
                'roi': roi
            }
        )
        return self.calculate_features_return_value

    def get_calculate_features_called_with_parameters(self) -> List[Dict[Optional[str], Any]]:
        return self.calculate_features_called_with_parameters

    def set_calculate_features_return_value(self, return_value: Any) -> None:
        self.calculate_features_return_value = return_value
