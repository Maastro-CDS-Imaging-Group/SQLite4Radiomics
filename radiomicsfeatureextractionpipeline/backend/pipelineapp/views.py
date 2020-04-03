import os

from shutil import make_archive
from shutil import rmtree
from wsgiref.util import FileWrapper
import threading
import src.calculate.calculation_script as calc

# from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.db import connection
# from rest_framework.parsers import JSONParser
from rest_framework import status
from django.conf import settings
from subprocess import Popen
import json
# import copy

# from pipelineapp.models import *
from pipelineapp.serializers import *

calculator: calc.Calculator = calc.Calculator()
calculator_copy: calc.Calculator = calculator

# Create your views here.

# REST METHODS
# Get data to view in front end table
# csrf_exempt allows the requests to be executed without a session token.
# When safe=False in the JSON responses, this allows for passing any data in the response, as long as they are objects
@csrf_exempt
def image_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMImages
    """
    if request.method == 'GET':
        images = Dicomimages.objects.all()
        images_serializer = DicomImageSerializer(images, many=True)
        return JsonResponse(images_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def patient_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMPatient
    """
    if request.method == 'GET':
        patients = Dicompatients.objects.all()
        patients_serializer = DicomPatientSerializer(patients, many=True)
        return JsonResponse(patients_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def radiomic_class_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMRadiomicClass
    """
    if request.method == 'GET':
        radiomic_class = Dicomradiomicclass .objects.all()
        radiomic_class_serializer = DicomRadiomicClassSerializer(
            radiomic_class, many=True)
        return JsonResponse(radiomic_class_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def feature_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMFeature
    """
    if request.method == 'GET':
        features = Dicomradiomicfeature.objects.all()
        features_serializer = DicomRadiomicFeatureSerializer(features, many=True)
        return JsonResponse(features_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def feature_value_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMFeatureValue
    """
    if request.method == 'GET':
        feature_value = Dicomradiomicfeaturevalue.objects.all()
        feature_value_serializer = DicomRadiomicFeaturevalueSerializer(
            feature_value, many=True)
        return JsonResponse(feature_value_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def radiomic_filter_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMRadiomicFilter
    """
    if request.method == 'GET':
        radiomic_filter = Dicomradiomicfilter.objects.all()
        radiomic_filter_serializer = DicomRadiomicFilterSerializer(
            radiomic_filter, many=True)
        return JsonResponse(radiomic_filter_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def radiomics_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMRadiomics
    """
    if request.method == 'GET':
        radiomics = Dicomradiomics.objects.all()
        radiomics_serializer = DicomRadiomicSerializer(radiomics, many=True)
        return JsonResponse(radiomics_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def roi_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMROI
    """
    if request.method == 'GET':
        roi = Dicomroi.objects.all()
        roi_serializer = DicomRoiSerializer(roi, many=True)
        return JsonResponse(roi_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def series_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMSeries
    """
    if request.method == 'GET':
        series = Dicomseries.objects.all()
        series_serializer = DicomSeriesSerializer(series, many=True)
        return JsonResponse(series_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()

@csrf_exempt
def series_roi_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMSeriesROI
    """
    if request.method == 'GET':
        series_roi = Dicomseriesroi.objects.all()
        series_roi_serializer = DicomSeriesRoiSerializer(series_roi, many=True)
        return JsonResponse(series_roi_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def study_list(request):
    """
        Takes a GET request a returns a JSON response with the data from DICOMStudy
    """
    if request.method == 'GET':
        studies = Dicomstudies.objects.all()
        studies_serializer = DicomStudiesSerializer(studies, many=True)
        return JsonResponse(studies_serializer.data, safe=False)
    else:
        return HttpResponseBadRequest()

@csrf_exempt
def general_overview(request):
    """
        Takes a GET request a returns a JSON response with the data from the query
    """
    if request.method == 'GET':
        with open("resources/queries/sqlite/general_overview.sql", 'r') as q:
            query_file = q.read()
        with connection.cursor() as cursor:
            cursor.execute(query_file)
            columns = [col[0] for col in cursor.description]
            overview = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return JsonResponse(overview, safe=False)
    else:
        return HttpResponseBadRequest()

# Open file functions
# These functions handle file reading
@csrf_exempt
def open_parameter_file(request):
    """
        Takes a GET request.
        Opens the yaml file in read mode and returns the contents of the file in an HTTP response
    """
    if request.method == 'GET':
        open_file = open(os.path.join(settings.BASE_DIR, 'resources/Pyradiomics_Params.yaml'), 'r')
        return HttpResponse(open_file)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def open_config_file(request):
    """
        Takes a GET request.
        Opens the config.ini file in read mode and returns the contents of the file in an HTTP response
    """
    if request.method == 'GET':
        open_file = open(os.path.join(settings.BASE_DIR, 'resources/config.ini'), 'r')
        return HttpResponse(open_file)
    else:
        return HttpResponseBadRequest()


# These functions handle writing to files
@csrf_exempt
def write_to_config_file(request):
    """
        Takes a PUT request.
        First opens the config.ini file in read mode and writes it to the an 'old' file,
        which serves as a previous version for restoring.
        It then opens the config.ini file in overwrite mode and writes the contents from the request to the file.
        Returns an OK status response upon successful writing.
    """
    if request.method == 'PUT':
        text = request.body.decode("utf-8")
        open_file = open(os.path.join(settings.BASE_DIR, 'resources/config.ini'), 'r')
        with open(os.path.join(settings.BASE_DIR, 'resources/backups/old.ini'), 'w+') as previous:
            previous.write(open_file.read())
        with open(os.path.join(settings.BASE_DIR, 'resources/config.ini'), 'w+') as f:
            f.write(text)
        global calculator
        calculator = calc.Calculator()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def write_to_parameter_file(request):
    """
        Takes a PUT request.
        First opens the yaml file in read mode and writes it to the an 'old' file,
        which serves as a previous version for restoring.
        It then opens the yaml file in overwrite mode and writes the contents from the request to the file.
        Returns an OK status response upon successful writing.
    """
    if request.method == 'PUT':
        text = request.body.decode("utf-8")
        open_file = open(os.path.join(settings.BASE_DIR, 'resources/Pyradiomics_Params.yaml'), 'r')
        with open(os.path.join(settings.BASE_DIR, 'resources/backups/old.yaml'), 'w+') as previous:
            previous.write(open_file.read())
        with open(os.path.join(settings.BASE_DIR, 'resources/Pyradiomics_Params.yaml'), 'w+') as f:
            f.write(text)
        global calculator
        calculator = calc.Calculator()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


# Functions that handle file restoration
@csrf_exempt
def restore_default_config_file(request):
    """
        Takes a PUT request.
        First opens the default configuration file in read mode.
        It then opens the config.ini file in overwrite mode and writes the contents from the default file.
        Returns an OK status response upon successful writing.
    """
    if request.method == 'PUT':
        open_default = open(os.path.join(settings.BASE_DIR, 'resources/backups/default.ini'), 'r')
        with open(os.path.join(settings.BASE_DIR, 'resources/config.ini'), 'w+') as restored:
            restored.write(open_default.read())
            restored.seek(0)
        global calculator
        calculator = calc.Calculator()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def restore_default_parameter_file(request):
    """
        Takes a PUT request.
        First opens the default parameter file in read mode.
        It then opens the yaml file in overwrite mode and writes the contents from the default file.
        Returns an OK status response upon successful writing.
    """
    if request.method == 'PUT':
        open_default = open(os.path.join(settings.BASE_DIR, 'resources/backups/default.yaml'), 'r')
        with open(os.path.join(settings.BASE_DIR, 'resources/Pyradiomics_Params.yaml'), 'w+') as restored:
            restored.write(open_default.read())
            restored.seek(0)
        global calculator
        calculator = calc.Calculator()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def restore_old_config_file(request):
    """
        Takes a PUT request.
        First opens the old configuration file (or previous version) in read mode.
        It then opens the config.ini file in overwrite mode and writes the contents from the old file.
        Returns an OK status response upon successful writing.
    """
    if request.method == 'PUT':
        open_default = open(os.path.join(settings.BASE_DIR, 'resources/backups/old.ini'), 'r')
        with open(os.path.join(settings.BASE_DIR, 'resources/config.ini'), 'w+') as restored:
            restored.write(open_default.read())
            restored.seek(0)
        global calculator
        calculator = calc.Calculator()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def restore_old_parameter_file(request):
    """
        Takes a PUT request.
        First opens the old parameter file (or previous version) in read mode.
        It then opens the yaml file in overwrite mode and writes the contents from the old file.
        Returns an OK status response upon successful writing.
    """
    if request.method == 'PUT':
        open_old = open(os.path.join(settings.BASE_DIR, 'resources/backups/old.yaml'), 'r')
        with open(os.path.join(settings.BASE_DIR, 'resources/Pyradiomics_Params.yaml'), 'w+') as restored:
            restored.write(open_old.read())
            restored.seek(0)
        global calculator
        calculator = calc.Calculator()
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


# Run priority setter
@csrf_exempt
def priority_setter(request):
    """
        Takes a GET request.
        Executes batch file.
        Returns OK status response
    """
    if request.method == 'GET':
        Popen(os.path.join('start ' + settings.BASE_DIR, 'resources/priority_setter_django.bat'), shell=True)
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


# Run recreate database tables
@csrf_exempt
def recreate_radiomic_tables(request):
    """
        Takes a GET request.
        Opens query files for deleting and creating the radiomic tables in read mode.
        Opens connection to the database and executes the queries in the right order.
        Returns OK status response upon successful execution
    """
    if request.method == 'GET':
        with open("resources/queries/sqlite/delete_tables_from_database.sql", 'r') as q:
            delete_radiomics_tables_query = q.read()
        with open("resources/queries/sqlite/roi/create_roi_table.sql", 'r') as q:
            create_roi_table_query = q.read()
        with open("resources/queries/sqlite/roi_series/create_series_roi_table2.sql", 'r') as q:
            create_seriesroi_table_query = q.read()
        with open("resources/queries/sqlite/radiomics/create_radiomics_tables2.sql", 'r') as q:
            create_radiomics_tables_query = q.read()

        with connection.cursor() as cursor:
            cursor.executescript(delete_radiomics_tables_query)
            cursor.executescript(create_roi_table_query)
            cursor.executescript(create_seriesroi_table_query)
            cursor.executescript(create_radiomics_tables_query)

        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


# Functions used for zipping files and downloading them
@csrf_exempt
def download_csv_files(request, file_name=""):
    """
        Takes a GET request.
        Uses the 'out' folder. Creates a zip file of the contents within the 'out' folder.
        Returns the zip file in the response
    """
    if request.method == 'GET':
        try:
            files_path = "out"
            path_to_zip = make_archive(files_path, "zip", files_path)
            response = HttpResponse(FileWrapper(open(path_to_zip, 'rb')), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
                filename=file_name.replace(" ", "_")
            )
        except (FileNotFoundError):
            return HttpResponseNotFound()
        else:
            return response
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def download_log_files(request, file_name=""):
    """
        Takes a GET request.
        Uses the 'logs' folder. Creates a zip file of the contents within the 'logs' folder.
        Returns the zip file in the response
    """
    if request.method == 'GET':
        try:
            files_path = "logs"
            path_to_zip = make_archive(files_path, "zip", files_path)
            response = HttpResponse(FileWrapper(open(path_to_zip, 'rb')), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="{filename}.zip"'.format(
                filename=file_name.replace(" ", "_")
            )
        except (FileNotFoundError):
            return HttpResponseNotFound()
        else:
            return response
    else:
        return HttpResponseBadRequest()


# Functions that handle calculations
@csrf_exempt
def get_calculations(request):
    """
        Takes a GET request.
        Opens query file for getting calculations by unique parameter and date in read mode.
        Opens connection to the database and executes the query.
        The results are pushed to a list.
        Returns the list in the response.
    """
    if request.method == 'GET':
        with open("resources/queries/sqlite/get_calculation_by_parameters_and_date.sql", 'r') as q:
            query_file = q.read()
        with connection.cursor() as cursor:
            cursor.execute(query_file)
            columns = [col[0] for col in cursor.description]
            calculations = [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]
        return JsonResponse(calculations, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def delete_calculation(request):
    """
        Takes a POST request.
        Decodes request and uses it as input for a raw query.
        Opens connection to the database and executes the query.
        The results are pushed to a list.
        Each calculation in the list is then deleted from the correct tables.
        Returns OK status response upon successful execution.
    """
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        radiomic_calc = []
        query = "select distinct df.radiomicsid from Dicomradiomicfeaturevalue as df join Dicomradiomics as dr on dr.radiomicsid=df.radiomicsid where df.value like %s and dr.timeofcalculation like %s"
        for c in body:
            with connection.cursor() as cursor:
                cursor.execute(query, tuple([c['Value'], c['calculation_date']+'%']))
                pat_data = cursor.fetchall()
                for row in pat_data:
                    print(row[0])
                    radiomic_calc.append(row[0])
            for r_id in radiomic_calc:
                print(r_id)
                Dicomradiomics.objects.filter(radiomicsid=r_id).delete()
                Dicomradiomicfeaturevalue.objects.filter(radiomicsid=r_id).delete()
        return HttpResponse(status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()
        

# Functions used in feature extraction process
@csrf_exempt
def start_recalculate(request):
    """
        Takes a GET request.
        Sets the query type to default -  calculate for any data that has not been extracted yet.
        Passes the extraction process to a thread and starts it.
        Returns a JSON response with a message.
    """
    if request.method == 'GET':
        global calculator_copy
        global calculator
        calculator_copy = calculator
        calculator_copy.set_query_type_default()
        t = threading.Thread(target=calculator_copy.main)
        t.start()
        return JsonResponse({'text': 'Process starting...'}, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def cancel(request):
    """
        Takes a GET request.
        Sets the process state to cancelled.
        Returns a JSON response with a message.
    """
    if request.method == 'GET':
        calculator_copy.set_cancelled()
        return JsonResponse({'text': 'Process is being cancelled...'}, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def progress(request):
    """
        Takes a GET request.
        Returns a JSON response with a progress message.
    """
    if request.method == 'GET':
        return JsonResponse({'text': calculator_copy.get_progress()}, safe=False)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def start_calculate(request):
    """
        Takes a GET request.
        Sets the query type to update -  perform feature extraction on all stored data.
        Passes the extraction process to a thread and starts it.
        Returns a JSON response with a message.
    """
    if request.method == 'GET':
        global calculator_copy
        global calculator
        calculator_copy = calculator
        calculator.set_query_type_update()
        t = threading.Thread(target=calculator_copy.main)
        t.start()
        return JsonResponse({'text': 'Process starting...'}, safe=False)
    else:
        return HttpResponseBadRequest()


# Updates the values for the ROI priorities
@csrf_exempt
def update_priority(request):
    """
        Takes a POST request.
        Decodes request and uses it as input for a raw query.
        Opens connection to the database and executes the query.
        Each priority value is then updated.
        Returns OK status response upon successful execution.
    """
    if request.method == 'POST':
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        query = "UPDATE Dicomroi SET priority = %s WHERE roiid = %s"
        for c in body:
            with connection.cursor() as cursor:
                cursor.execute(query, tuple([c['priority'], c['roiid']]))
        return HttpResponse(status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()

# Set csv saving method
@csrf_exempt
def save_all(request):
    """
        Takes a GET request.
        Calls the method to change the boolean for dumping all data into one single CSV file to TRUE
        Returns OK status response upon successful execution.
    """
    if request.method == 'GET':
        calculator.set_csv_save_to_dump_all()
        return HttpResponse(status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def save_individual(request):
    """
        Takes a GET request.
        Calls the method to change the boolean for dumping all data into one single CSV file to FALSE
        Returns OK status response upon successful execution.
    """
    if request.method == 'GET':
        calculator.set_csv_save_to_dump_individual()
        return HttpResponse(status.HTTP_200_OK)
    else:
        return HttpResponseBadRequest()


# Delete output folder and all csv's within
@csrf_exempt
def delete_csv_files(request):
    """
        Takes a GET request.
        Calls the method to change the boolean for dumping all data into one single CSV file to FALSE
        Returns OK status response upon successful execution.
    """
    if request.method == 'GET':
        try:
            rmtree('out')
            os.remove("out.zip")
        except (FileNotFoundError):
            return HttpResponseNotFound()
        else:
            return HttpResponse(status.HTTP_200_OK)

    else:
        return HttpResponseBadRequest()

# Tell frontend that backend is online
@csrf_exempt
def pong(request):
    if request.method == 'GET':
        return JsonResponse('pong', safe=False)
    else:
        return HttpResponseBadRequest()
