select di.SOPInstanc
from DICOMImages as di inner join DICOMSeries as ds on di.SeriesInst = ds.SeriesInst
where lower(ds.Modality)='rtstruct';