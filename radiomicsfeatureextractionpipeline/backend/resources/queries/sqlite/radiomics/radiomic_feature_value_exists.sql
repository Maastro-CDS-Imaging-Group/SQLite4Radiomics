SELECT *
FROM DICOMRadiomicFeatureValue
WHERE RadiomicsId = :radiomics_id AND RoiId = :roi_id AND FilterId = :radiomic_filter_id AND
 ClassId = :radiomic_class_id AND FeatureId = :radiomic_feature_id