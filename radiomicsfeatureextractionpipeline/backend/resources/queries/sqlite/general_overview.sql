select
PatientID as Patient_ID, PatientNam as Patient_Name, PatientSex as Patient_Sex, 

(select dt.PatientsAg from dicomstudies as dt where dt.PatientID = dicompatients.patientid ) as Patient_Age,

(select count(*) from dicomseries as ds where ds.seriespat = dicompatients.patientid and ds.modality='RTSTRUCT') as RTStructs,

(select count(*) from dicomseries as ds where ds.seriespat = dicompatients.patientid and ds.modality='RTDOSE') as RTDoses,

(select count(*) from dicomseries as ds where ds.seriespat = dicompatients.patientid and ds.modality='RTPLAN') as RTPlans,

(select count(*) from dicomseries as ds join DICOMImages as di on ds.seriespat = di.ImagePat and di.ImagePat=PatientID where upper(ds.modality)='CT') as CT_Scans,

(select count(*) from dicomseries as ds join DICOMImages as di on ds.seriespat = di.ImagePat and di.ImagePat=PatientID where upper(ds.modality)='MR') as MR_Scans,

(select count(*) from dicomseries as ds join DICOMImages as di on ds.seriespat = di.ImagePat and di.ImagePat=PatientID where upper(ds.modality)='PT') as PET_Scans,

(select count(*) from dicomradiomics as dr where dr.radiomicpat = dicompatients.patientid ) as Radiomics_Calculations

from dicompatients

group by patientid;
