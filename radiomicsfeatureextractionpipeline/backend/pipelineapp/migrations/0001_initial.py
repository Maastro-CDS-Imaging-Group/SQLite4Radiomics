# Generated by Django 2.2.5 on 2019-09-24 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dicomimages',
            fields=[
                ('sopinstanc', models.CharField(db_column='SOPInstanc', max_length=64, primary_key=True, serialize=False)),
                ('sopclassui', models.CharField(blank=True, db_column='SOPClassUI', max_length=64, null=True)),
                ('imagenumbe', models.CharField(blank=True, db_column='ImageNumbe', max_length=12, null=True)),
                ('imagedate', models.CharField(blank=True, db_column='ImageDate', max_length=8, null=True)),
                ('imagetime', models.CharField(blank=True, db_column='ImageTime', max_length=16, null=True)),
                ('echonumber', models.CharField(blank=True, db_column='EchoNumber', max_length=64, null=True)),
                ('numberoffr', models.CharField(blank=True, db_column='NumberOfFr', max_length=12, null=True)),
                ('acqdate', models.CharField(blank=True, db_column='AcqDate', max_length=8, null=True)),
                ('acqtime', models.CharField(blank=True, db_column='AcqTime', max_length=16, null=True)),
                ('receivingc', models.CharField(blank=True, db_column='ReceivingC', max_length=16, null=True)),
                ('acqnumber', models.CharField(blank=True, db_column='AcqNumber', max_length=12, null=True)),
                ('slicelocat', models.CharField(blank=True, db_column='SliceLocat', max_length=16, null=True)),
                ('samplesper', models.CharField(blank=True, db_column='SamplesPer', max_length=5, null=True)),
                ('photometri', models.CharField(blank=True, db_column='PhotoMetri', max_length=16, null=True)),
                ('rows', models.CharField(blank=True, db_column='Rows', max_length=5, null=True)),
                ('colums', models.CharField(blank=True, db_column='Colums', max_length=5, null=True)),
                ('bitsstored', models.CharField(blank=True, db_column='BitsStored', max_length=5, null=True)),
                ('imagetype', models.CharField(blank=True, db_column='ImageType', max_length=128, null=True)),
                ('imageid', models.CharField(blank=True, db_column='ImageID', max_length=16, null=True)),
                ('imagepat', models.CharField(blank=True, db_column='ImagePat', max_length=64, null=True)),
                ('seriesinst', models.CharField(blank=True, db_column='SeriesInst', max_length=64, null=True)),
                ('accesstime', models.IntegerField(blank=True, db_column='AccessTime', null=True)),
                ('qtimestamp', models.IntegerField(blank=True, db_column='qTimeStamp', null=True)),
                ('qflags', models.IntegerField(blank=True, db_column='qFlags', null=True)),
                ('qspare', models.CharField(blank=True, db_column='qSpare', max_length=64, null=True)),
                ('objectfile', models.CharField(blank=True, db_column='ObjectFile', max_length=255, null=True)),
                ('devicename', models.CharField(blank=True, db_column='DeviceName', max_length=32, null=True)),
            ],
            options={
                'db_table': 'DICOMImages',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicompatients',
            fields=[
                ('patientid', models.CharField(db_column='PatientID', max_length=64, primary_key=True, serialize=False)),
                ('patientnam', models.CharField(blank=True, db_column='PatientNam', max_length=64, null=True)),
                ('patientbir', models.CharField(blank=True, db_column='PatientBir', max_length=8, null=True)),
                ('patientsex', models.CharField(blank=True, db_column='PatientSex', max_length=16, null=True)),
                ('accesstime', models.IntegerField(blank=True, db_column='AccessTime', null=True)),
                ('qtimestamp', models.IntegerField(blank=True, db_column='qTimeStamp', null=True)),
                ('qflags', models.IntegerField(blank=True, db_column='qFlags', null=True)),
                ('qspare', models.CharField(blank=True, db_column='qSpare', max_length=64, null=True)),
            ],
            options={
                'db_table': 'DICOMPatients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomradiomicclass',
            fields=[
                ('classid', models.AutoField(db_column='ClassId', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
            ],
            options={
                'db_table': 'DICOMRadiomicClass',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomradiomicfeature',
            fields=[
                ('radiomicfeatureid', models.AutoField(db_column='RadiomicFeatureId', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
            ],
            options={
                'db_table': 'DICOMRadiomicFeature',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomradiomicfeaturevalue',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('value', models.TextField(db_column='Value')),
            ],
            options={
                'db_table': 'DICOMRadiomicFeatureValue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomradiomicfilter',
            fields=[
                ('filterid', models.AutoField(db_column='FilterId', primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
            ],
            options={
                'db_table': 'DICOMRadiomicFilter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomradiomics',
            fields=[
                ('radiomicsid', models.AutoField(db_column='RadiomicsId', primary_key=True, serialize=False)),
                ('radiomicseriesofimageslicesmodality', models.TextField(db_column='RadiomicSeriesOfImageSlicesModality')),
                ('timeofcalculation', models.TextField(blank=True, db_column='TimeOfCalculation', null=True)),
            ],
            options={
                'db_table': 'DICOMRadiomics',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomroi',
            fields=[
                ('roiid', models.AutoField(db_column='RoiId', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='Name', max_length=64, null=True)),
                ('priority', models.IntegerField(blank=True, db_column='Priority', null=True)),
            ],
            options={
                'db_table': 'DICOMROI',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomseries',
            fields=[
                ('seriesinst', models.CharField(db_column='SeriesInst', max_length=64, primary_key=True, serialize=False)),
                ('seriesnumb', models.CharField(blank=True, db_column='SeriesNumb', max_length=12, null=True)),
                ('seriesdate', models.CharField(blank=True, db_column='SeriesDate', max_length=8, null=True)),
                ('seriestime', models.CharField(blank=True, db_column='SeriesTime', max_length=16, null=True)),
                ('seriesdesc', models.CharField(blank=True, db_column='SeriesDesc', max_length=64, null=True)),
                ('modality', models.CharField(blank=True, db_column='Modality', max_length=16, null=True)),
                ('patientpos', models.CharField(blank=True, db_column='PatientPos', max_length=16, null=True)),
                ('contrastbo', models.CharField(blank=True, db_column='ContrastBo', max_length=64, null=True)),
                ('manufactur', models.CharField(blank=True, db_column='Manufactur', max_length=64, null=True)),
                ('modelname', models.CharField(blank=True, db_column='ModelName', max_length=64, null=True)),
                ('bodypartex', models.CharField(blank=True, db_column='BodyPartEx', max_length=64, null=True)),
                ('protocolna', models.CharField(blank=True, db_column='ProtocolNa', max_length=64, null=True)),
                ('stationnam', models.CharField(blank=True, db_column='StationNam', max_length=16, null=True)),
                ('institutio', models.CharField(blank=True, db_column='Institutio', max_length=64, null=True)),
                ('frameofref', models.CharField(blank=True, db_column='FrameOfRef', max_length=64, null=True)),
                ('seriespat', models.CharField(blank=True, db_column='SeriesPat', max_length=64, null=True)),
                ('studyinsta', models.CharField(blank=True, db_column='StudyInsta', max_length=64, null=True)),
                ('accesstime', models.IntegerField(blank=True, db_column='AccessTime', null=True)),
                ('qtimestamp', models.IntegerField(blank=True, db_column='qTimeStamp', null=True)),
                ('qflags', models.IntegerField(blank=True, db_column='qFlags', null=True)),
                ('qspare', models.CharField(blank=True, db_column='qSpare', max_length=64, null=True)),
            ],
            options={
                'db_table': 'DICOMSeries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomseriesroi',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('number', models.IntegerField(db_column='Number')),
                ('dicomsegfile', models.CharField(blank=True, db_column='DicomSegFile', max_length=64, null=True)),
            ],
            options={
                'db_table': 'DICOMSeriesROI',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dicomstudies',
            fields=[
                ('studyinsta', models.CharField(db_column='StudyInsta', max_length=64, primary_key=True, serialize=False)),
                ('studydate', models.CharField(blank=True, db_column='StudyDate', max_length=8, null=True)),
                ('studytime', models.CharField(blank=True, db_column='StudyTime', max_length=16, null=True)),
                ('studyid', models.CharField(blank=True, db_column='StudyID', max_length=16, null=True)),
                ('studydescr', models.CharField(blank=True, db_column='StudyDescr', max_length=64, null=True)),
                ('accessionn', models.CharField(blank=True, db_column='AccessionN', max_length=16, null=True)),
                ('referphysi', models.CharField(blank=True, db_column='ReferPhysi', max_length=64, null=True)),
                ('patientsag', models.CharField(blank=True, db_column='PatientsAg', max_length=16, null=True)),
                ('patientswe', models.CharField(blank=True, db_column='PatientsWe', max_length=16, null=True)),
                ('studymodal', models.CharField(blank=True, db_column='StudyModal', max_length=64, null=True)),
                ('patientnam', models.CharField(blank=True, db_column='PatientNam', max_length=64, null=True)),
                ('patientbir', models.CharField(blank=True, db_column='PatientBir', max_length=8, null=True)),
                ('patientsex', models.CharField(blank=True, db_column='PatientSex', max_length=16, null=True)),
                ('patientid', models.CharField(blank=True, db_column='PatientID', max_length=64, null=True)),
                ('accesstime', models.IntegerField(blank=True, db_column='AccessTime', null=True)),
                ('qtimestamp', models.IntegerField(blank=True, db_column='qTimeStamp', null=True)),
                ('qflags', models.IntegerField(blank=True, db_column='qFlags', null=True)),
                ('qspare', models.CharField(blank=True, db_column='qSpare', max_length=64, null=True)),
            ],
            options={
                'db_table': 'DICOMStudies',
                'managed': False,
            },
        ),
    ]
