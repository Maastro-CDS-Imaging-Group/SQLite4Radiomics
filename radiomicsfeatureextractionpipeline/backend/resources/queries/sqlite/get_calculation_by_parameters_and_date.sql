select DISTINCT df.Value, strftime('%Y-%m-%d', dr.TimeOfCalculation) as calculation_date
from DICOMRadiomicFeatureValue as df join DICOMRadiomics as dr on dr.RadiomicsId = df.RadiomicsId
where df.Value like "{'m%";