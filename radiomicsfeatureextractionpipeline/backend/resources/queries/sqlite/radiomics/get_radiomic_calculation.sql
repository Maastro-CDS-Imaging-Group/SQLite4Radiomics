SELECT *
FROM DICOMRadiomics
WHERE RadiomicPat = :patient_id AND RadiomicRtstructSeries = :rtstruct_series_id AND RadiomicSeriesOfImageSlices = :series_image_slices_id