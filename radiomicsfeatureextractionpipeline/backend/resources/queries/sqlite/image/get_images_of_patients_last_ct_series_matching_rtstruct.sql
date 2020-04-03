SELECT ImageRtstruct.ImagePat AS 'patient_id', SeriesRtstruct.StudyInsta AS 'study_id',
    ImageRtstruct.SeriesInst AS 'rtstruct_series_id', ImageRtstruct.ObjectFile AS 'rtstruct_file',
    SeriesOfImageSlices.SeriesInst AS 'series_of_slices_id', ImageSlices.ObjectFile AS 'image_slice_id'
FROM DICOMImages ImageRtstruct, DICOMSeries SeriesRtstruct, DICOMSeries SeriesOfImageSlices, DICOMImages ImageSlices
WHERE ImageRtstruct.SOPInstanc = :image_id AND (SeriesOfImageSlices.Modality = 'CT' OR SeriesOfImageSlices.Modality = 'PT' OR SeriesOfImageSlices.Modality = 'MR')
    AND ImageRtstruct.SeriesInst = SeriesRtstruct.SeriesInst
    AND SeriesOfImageSlices.StudyInsta = SeriesRtstruct.StudyInsta AND ImageSlices.SeriesInst = SeriesOfImageSlices.SeriesInst
ORDER BY ImageRtstruct.ImagePat, SeriesRtstruct.StudyInsta, ImageRtstruct.SeriesInst, SeriesOfImageSlices.SeriesInst,
CAST(ImageSlices.ImageNumbe AS INTEGER)