SELECT *
FROM DICOMROI
WHERE RoiId IN
    (SELECT RoiId
     FROM DICOMSeriesROI
     WHERE SeriesInst = :series_id)
ORDER BY Priority