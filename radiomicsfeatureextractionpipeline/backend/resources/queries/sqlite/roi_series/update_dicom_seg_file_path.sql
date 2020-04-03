UPDATE DICOMSeriesROI
SET DicomSegFile = :dicom_seg_file
WHERE RoiId = :roi_id AND SeriesInst = :series_id