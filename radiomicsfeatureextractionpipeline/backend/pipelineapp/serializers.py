from rest_framework import serializers
from pipelineapp.models import *


class DicomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomimages
        fields = ['imagepat', 'sopinstanc', 'sopclassui', 'imagenumbe', 'imagedate', 'imagetime', 'echonumber',
                  'numberoffr', 'acqdate', 'acqtime', 'acqnumber', 'slicelocat', 'samplesper', 'photometri',
                  'rows', 'colums', 'bitsstored', 'imagetype', 'imageid', 'seriesinst', 'objectfile', 'devicename']


class DicomPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicompatients
        fields = ['patientid', 'patientnam', 'patientbir',
                  'patientsex']


class DicomRoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomroi
        fields = ['roiid', 'name', 'priority']


class DicomRadiomicClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomradiomicclass
        fields = ['classid', 'parentclassid', 'name']


class DicomRadiomicFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomradiomicfeature
        fields = ['radiomicfeatureid', 'radiomicclassid', 'name']


class DicomRadiomicFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomradiomicfilter
        fields = ['filterid', 'name']


class DicomRadiomicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomradiomics
        fields = ['radiomicsid', 'radiomicpat', 'radiomicseriesofimageslicesmodality',
                  'radiomicseriesofimageslices', 'radiomicrtstructseries', 'timeofcalculation']


class DicomSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomseries
        fields = ['seriespat', 'seriesinst', 'seriesnumb', 'seriesdate', 'seriestime', 'seriesdesc', 'modality',
                  'patientpos', 'contrastbo', 'manufactur', 'modelname', 'bodypartex', 'protocolna', 'stationnam',
                  'institutio', 'frameofref', 'studyinsta']


class DicomStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomstudies
        fields = ['patientnam', 'studyinsta', 'studydate', 'studytime', 'studyid', 'studydescr', 'accessionn', 'referphysi',
                  'patientsag', 'patientswe', 'studymodal', 'patientbir', 'patientsex', 'patientid']


class DicomSeriesRoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomseriesroi
        fields = ['id', 'roiid', 'seriesinst', 'number', 'dicomsegfile']


class DicomRadiomicFeaturevalueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dicomradiomicfeaturevalue
        fields = ['id', 'radiomicsid', 'roiid', 'filterid',
                  'classid', 'featureid', 'value']
