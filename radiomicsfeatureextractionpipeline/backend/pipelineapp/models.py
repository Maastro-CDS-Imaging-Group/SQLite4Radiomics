# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dicomimages(models.Model):
    # Field name made lowercase.
    sopinstanc = models.CharField(
        db_column='SOPInstanc', primary_key=True, max_length=64)
    # Field name made lowercase.
    sopclassui = models.CharField(
        db_column='SOPClassUI', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    imagenumbe = models.CharField(
        db_column='ImageNumbe', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    imagedate = models.CharField(
        db_column='ImageDate', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    imagetime = models.CharField(
        db_column='ImageTime', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    echonumber = models.CharField(
        db_column='EchoNumber', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    numberoffr = models.CharField(
        db_column='NumberOfFr', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    acqdate = models.CharField(
        db_column='AcqDate', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    acqtime = models.CharField(
        db_column='AcqTime', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    receivingc = models.CharField(
        db_column='ReceivingC', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    acqnumber = models.CharField(
        db_column='AcqNumber', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    slicelocat = models.CharField(
        db_column='SliceLocat', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    samplesper = models.CharField(
        db_column='SamplesPer', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    photometri = models.CharField(
        db_column='PhotoMetri', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    rows = models.CharField(
        db_column='Rows', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    colums = models.CharField(
        db_column='Colums', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    bitsstored = models.CharField(
        db_column='BitsStored', max_length=5, blank=True, null=True)
    # Field name made lowercase.
    imagetype = models.CharField(
        db_column='ImageType', max_length=128, blank=True, null=True)
    # Field name made lowercase.
    imageid = models.CharField(
        db_column='ImageID', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    imagepat = models.CharField(
        db_column='ImagePat', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    seriesinst = models.CharField(
        db_column='SeriesInst', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    accesstime = models.IntegerField(
        db_column='AccessTime', blank=True, null=True)
    # Field name made lowercase.
    qtimestamp = models.IntegerField(
        db_column='qTimeStamp', blank=True, null=True)
    # Field name made lowercase.
    qflags = models.IntegerField(db_column='qFlags', blank=True, null=True)
    # Field name made lowercase.
    qspare = models.CharField(
        db_column='qSpare', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    objectfile = models.CharField(
        db_column='ObjectFile', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    devicename = models.CharField(
        db_column='DeviceName', max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DICOMImages'


class Dicompatients(models.Model):
    # Field name made lowercase.
    patientid = models.CharField(
        db_column='PatientID', primary_key=True, max_length=64)
    # Field name made lowercase.
    patientnam = models.CharField(
        db_column='PatientNam', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    patientbir = models.CharField(
        db_column='PatientBir', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    patientsex = models.CharField(
        db_column='PatientSex', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    accesstime = models.IntegerField(
        db_column='AccessTime', blank=True, null=True)
    # Field name made lowercase.
    qtimestamp = models.IntegerField(
        db_column='qTimeStamp', blank=True, null=True)
    # Field name made lowercase.
    qflags = models.IntegerField(db_column='qFlags', blank=True, null=True)
    # Field name made lowercase.
    qspare = models.CharField(
        db_column='qSpare', max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DICOMPatients'


class Dicomroi(models.Model):
    # Field name made lowercase.
    roiid = models.AutoField(db_column='RoiId', primary_key=True, blank=True)
    # Field name made lowercase.
    name = models.CharField(
        db_column='Name', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DICOMROI'


class Dicomradiomicclass(models.Model):
    # Field name made lowercase.
    classid = models.AutoField(
        db_column='ClassId', primary_key=True, blank=True)
    # Field name made lowercase.
    parentclassid = models.ForeignKey(
        'self', models.DO_NOTHING, db_column='ParentClassId', blank=True, null=True)
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DICOMRadiomicClass'


class Dicomradiomicfeature(models.Model):
    # Field name made lowercase.
    radiomicfeatureid = models.AutoField(
        db_column='RadiomicFeatureId', primary_key=True, blank=True)
    # Field name made lowercase.
    radiomicclassid = models.ForeignKey(
        Dicomradiomicclass, models.DO_NOTHING, db_column='RadiomicClassId')
    name = models.TextField(db_column='Name') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DICOMRadiomicFeature'

class Dicomradiomicfilter(models.Model):
    # Field name made lowercase.
    filterid = models.AutoField(
        db_column='FilterId', primary_key=True, blank=True)
    name = models.TextField(db_column='Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DICOMRadiomicFilter'


class Dicomradiomics(models.Model):
    # Field name made lowercase.
    radiomicsid = models.AutoField(
        db_column='RadiomicsId', primary_key=True, blank=True)
    # Field name made lowercase.
    radiomicpat = models.ForeignKey(
        Dicompatients, on_delete=models.CASCADE, db_column='RadiomicPat')
    radiomicseriesofimageslicesmodality = models.TextField(
        db_column='RadiomicSeriesOfImageSlicesModality') 
    # Field name made lowercase.
    radiomicseriesofimageslices = models.ForeignKey(
        'Dicomseries', on_delete=models.CASCADE, db_column='RadiomicSeriesOfImageSlices', related_name='image_series_insta')  # Field name made lowercase.
    # Field name made lowercase.
    radiomicrtstructseries = models.ForeignKey(
        'Dicomseries', on_delete=models.CASCADE, db_column='RadiomicRtstructSeries', related_name='rtstruct_series_insta')
    # Field name made lowercase.
    timeofcalculation = models.TextField(
        db_column='TimeOfCalculation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DICOMRadiomics'


class Dicomseries(models.Model):
    # Field name made lowercase.
    seriesinst = models.CharField(
        db_column='SeriesInst', primary_key=True, max_length=64)
    # Field name made lowercase.
    seriesnumb = models.CharField(
        db_column='SeriesNumb', max_length=12, blank=True, null=True)
    # Field name made lowercase.
    seriesdate = models.CharField(
        db_column='SeriesDate', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    seriestime = models.CharField(
        db_column='SeriesTime', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    seriesdesc = models.CharField(
        db_column='SeriesDesc', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    modality = models.CharField(
        db_column='Modality', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    patientpos = models.CharField(
        db_column='PatientPos', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    contrastbo = models.CharField(
        db_column='ContrastBo', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    manufactur = models.CharField(
        db_column='Manufactur', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    modelname = models.CharField(
        db_column='ModelName', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    bodypartex = models.CharField(
        db_column='BodyPartEx', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    protocolna = models.CharField(
        db_column='ProtocolNa', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    stationnam = models.CharField(
        db_column='StationNam', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    institutio = models.CharField(
        db_column='Institutio', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    frameofref = models.CharField(
        db_column='FrameOfRef', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    seriespat = models.CharField(
        db_column='SeriesPat', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    studyinsta = models.CharField(
        db_column='StudyInsta', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    accesstime = models.IntegerField(
        db_column='AccessTime', blank=True, null=True)
    # Field name made lowercase.
    qtimestamp = models.IntegerField(
        db_column='qTimeStamp', blank=True, null=True)
    # Field name made lowercase.
    qflags = models.IntegerField(db_column='qFlags', blank=True, null=True)
    # Field name made lowercase.
    qspare = models.CharField(
        db_column='qSpare', max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DICOMSeries'

class Dicomstudies(models.Model):
    # Field name made lowercase.
    studyinsta = models.CharField(
        db_column='StudyInsta', primary_key=True, max_length=64)
    # Field name made lowercase.
    studydate = models.CharField(
        db_column='StudyDate', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    studytime = models.CharField(
        db_column='StudyTime', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    studyid = models.CharField(
        db_column='StudyID', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    studydescr = models.CharField(
        db_column='StudyDescr', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    accessionn = models.CharField(
        db_column='AccessionN', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    referphysi = models.CharField(
        db_column='ReferPhysi', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    patientsag = models.CharField(
        db_column='PatientsAg', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    patientswe = models.CharField(
        db_column='PatientsWe', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    studymodal = models.CharField(
        db_column='StudyModal', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    patientnam = models.CharField(
        db_column='PatientNam', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    patientbir = models.CharField(
        db_column='PatientBir', max_length=8, blank=True, null=True)
    # Field name made lowercase.
    patientsex = models.CharField(
        db_column='PatientSex', max_length=16, blank=True, null=True)
    # Field name made lowercase.
    patientid = models.CharField(
        db_column='PatientID', max_length=64, blank=True, null=True)
    # Field name made lowercase.
    accesstime = models.IntegerField(
        db_column='AccessTime', blank=True, null=True)
    # Field name made lowercase.
    qtimestamp = models.IntegerField(
        db_column='qTimeStamp', blank=True, null=True)
    # Field name made lowercase.
    qflags = models.IntegerField(db_column='qFlags', blank=True, null=True)
    # Field name made lowercase.
    qspare = models.CharField(
        db_column='qSpare', max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DICOMStudies'

class Dicomseriesroi(models.Model):
    id = models.AutoField(
        db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    # Field name made lowercase.
    roiid = models.ForeignKey(
        Dicomroi, models.DO_NOTHING, db_column='RoiId')
    # Field name made lowercase.
    seriesinst = models.ForeignKey(
        Dicomseries, models.DO_NOTHING, db_column='SeriesInst')
    # Field name made lowercase.
    number = models.IntegerField(db_column='Number')
    # Field name made lowercase.
    dicomsegfile = models.CharField(
        db_column='DicomSegFile', max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'DICOMSeriesROI'

class Dicomradiomicfeaturevalue(models.Model):
    id = models.AutoField(
        db_column='ID', primary_key=True, blank=True)  # Field name made lowercase.
    # Field name made lowercase.
    radiomicsid = models.ForeignKey( 
        Dicomradiomics, on_delete=models.CASCADE, db_column='RadiomicsId')
    # Field name made lowercase.
    roiid = models.ForeignKey(Dicomroi, on_delete=models.CASCADE, db_column='RoiId')
    # Field name made lowercase.
    filterid = models.ForeignKey(
        Dicomradiomicfilter, on_delete=models.CASCADE, db_column='FilterId')
    # Field name made lowercase.
    classid = models.ForeignKey(
        Dicomradiomicclass, on_delete=models.CASCADE, db_column='ClassId')
    # Field name made lowercase.
    featureid = models.ForeignKey(
        Dicomradiomicfeature, on_delete=models.CASCADE, db_column='FeatureId')
    value = models.TextField(db_column='Value')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DICOMRadiomicFeatureValue'
