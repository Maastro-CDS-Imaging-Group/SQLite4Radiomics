select PatientNam
from DICOMPatients
where PatientNam not in (
	select RadiomicPat
	from DICOMRadiomics
	where PatientNam=RadiomicPat);