from abc import ABC, abstractmethod

import SimpleITK as sitk
from radiomics import featureextractor

from dal.radiomic_feature_repository import RadiomicFeatureRepository
from logic.entities.radiomic_calculation import RadiomicCalculation
from logic.entities.roi import ROI


class FeatureCalculator(ABC):
    """
    Abstract base class for implementation of the strategy pattern.
    Used for extracting Radiomic features
    """

    def __init__(self, radiomic_feature_repos: RadiomicFeatureRepository, parameter_file: str) -> None:
        self.radiomic_feature_repos: RadiomicFeatureRepository = radiomic_feature_repos
        self.parameter_file: str = parameter_file

        self._extractor: featureextractor.RadiomicsFeaturesExtractor = featureextractor.RadiomicsFeaturesExtractor(parameter_file)
        #self._extractor.loadParams()

    @abstractmethod
    def calculate_features(self, radiomic_calculation: RadiomicCalculation, image: sitk.Image, mask: sitk.Image,
                           roi: ROI) -> None:
        pass
