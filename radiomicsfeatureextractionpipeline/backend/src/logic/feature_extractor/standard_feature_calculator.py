from typing import Dict, List

import SimpleITK as sitk

from dal.radiomic_feature_repository import RadiomicFeatureRepository
from logic.feature_extractor.feature_calculator import FeatureCalculator
from logic.entities.radiomic_class import RadiomicClass
from logic.entities.radiomic_feature import RadiomicFeature
from logic.entities.radiomic_feature_value import RadiomicFeatureValue
from logic.entities.radiomic_filter import RadiomicFilter
from logic.entities.roi import ROI


class StandardFeatureCalculator(FeatureCalculator):
    """
    Implementation of Strategy pattern for extraction radiomic features
    Implements Feature Extractor.
    """

    def __init__(self, radiomic_feature_repos: RadiomicFeatureRepository, parameter_file: str):
        super().__init__(radiomic_feature_repos, parameter_file)

    def calculate_features(self, radiomic_calculation, image: sitk.Image, mask: sitk.Image, roi: ROI) -> None:
        """

        :param radiomic_calculation:
        :param roi:
        :param image: 3d image used for feature extraction
        :param mask: binary mask used for feature extraction
        :return:
        """

        result: Dict[str, str] = self._extractor.execute(image, mask)
        feature: str
        value: str
        for feature, value in result.items():
            feature_description: List[str] = feature.split('_')

            radiomic_filter_name: str = feature_description[0]
            radiomic_class_name: str = feature_description[1]
            radiomic_feature_name: str = feature_description[2]

            feature_filter: RadiomicFilter = RadiomicFilter(radiomic_filter_name)
            self.radiomic_feature_repos.save_radiomic_filter(feature_filter)
            feature_filter: RadiomicFilter = self.radiomic_feature_repos.get_radiomic_filter_by_name(radiomic_filter_name)

            feature_class: RadiomicClass = RadiomicClass(radiomic_class_name)
            self.radiomic_feature_repos.save_radiomic_class(feature_class)
            feature_class: RadiomicClass = self.radiomic_feature_repos.get_radiomic_class_by_name(radiomic_class_name)

            feature: RadiomicFeature = RadiomicFeature(feature_class, radiomic_feature_name)
            self.radiomic_feature_repos.save_radiomic_feature(feature)
            feature: RadiomicFeature = self.radiomic_feature_repos.get_radiomic_feature_by_name(radiomic_feature_name)

            feature_value: RadiomicFeatureValue = RadiomicFeatureValue(roi, feature_filter, feature_class, feature, value)
            self.radiomic_feature_repos.save_radiomic_feature_value(radiomic_calculation, feature_value)
