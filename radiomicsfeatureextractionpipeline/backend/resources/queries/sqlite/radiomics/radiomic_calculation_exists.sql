SELECT *
FROM DICOMRadiomics
WHERE RadiomicPat = :patient_id AND RadiomicSeriesOfImageSlicesModality = :series_with_image_slices_modality AND
RadiomicSeriesOfImageSlices = :series_with_image_slices_id AND RadiomicRtstructSeries = :rtstruct_series_id AND
TimeOfCalculation = :time_of_calculation