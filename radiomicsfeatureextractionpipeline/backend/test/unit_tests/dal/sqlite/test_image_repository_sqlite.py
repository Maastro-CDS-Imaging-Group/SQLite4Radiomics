import os

from dal.sqlite.image_repository_sqlite import ImageRepositorySqlite
from logic.entities.ct_series import CtSeries
from logic.entities.image import Image
from logic.entities.patient import Patient
from logic.entities.pet_series import PetSeries
from logic.entities.rtstruct_series import RtstructSeries
from logic.entities.study import Study
from test.mock_ups.dal.sqlite.database_connector_sqlite import DatabaseConnectorSqliteMockUp
from test.mock_ups.dal.sqlite.patient_repository_sqlite import PatientRepositorySqliteMockUp
from test.mock_ups.dal.sqlite.series_repository_sqlite import SeriesRepositorySqliteMockUp
from test.mock_ups.dal.sqlite.study_repository_sqlite import StudyRepositorySqliteMockUp
from test.unit_tests.mocked_unit_tester import MockedUnitTester

import pandas as pd


class TestImageRepositorySqlite(MockedUnitTester):

    def setUp(self) -> None:
        queries_file_location: str = r"..\resources\queries\sqlite"
        self.database_connector = DatabaseConnectorSqliteMockUp(':memory:')
        self.series_repos = SeriesRepositorySqliteMockUp(self.database_connector, queries_file_location)
        self.patient_repos = PatientRepositorySqliteMockUp(self.database_connector, queries_file_location)
        self.study_repos = StudyRepositorySqliteMockUp(self.database_connector, queries_file_location)
        self.image_repos = ImageRepositorySqlite(self.database_connector, self.series_repos, self.patient_repos,
                                                 self.study_repos, queries_file_location)

    def test_get_all_images_of_series(self):
        method_to_test = self.image_repos.get_all_images_of_series
        outputs = [
            [
                Image('instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1', 'number_of_frames 1',
                      'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1', 'slice_location 1', 'samples_per 1',
                      'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1', 'image_type 1', 'identity 1',
                      'object_file 1', 'device_name 1'),
                Image('instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2', 'number_of_frames 2',
                      'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2', 'slice_location 2', 'samples_per 2',
                      'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2', 'image_type 2', 'identity 2',
                      'object_file 2', 'device_name 2')
            ],
            [
                Image('instance test', 'class_id test', 'number test', 'date test', 'time test', 'echo_number test',
                      'number_of_frames test', 'acq_date test', 'acq_time test', 'receiving_c test',
                      'acq_number test', 'slice_location test', 'samples_per test', 'photo_metric test',
                      'rows test', 'columns test', 'bits_stored test', 'image_type test', 'identity test',
                      'object_file test', 'device_name test'),
                Image('test instance', 'test class_id', 'test number', 'test date', 'test time', 'test echo_number',
                      'test number_of_frames', 'test acq_date', 'test acq_time', 'test receiving_c',
                      'test acq_number', 'test slice_location', 'test samples_per', 'test photo_metric',
                      'test rows', 'test columns', 'test bits_stored', 'test image_type', 'test identity',
                      'test object_file', 'test device_name'),
                Image('instance', 'class_id', 'number', 'date', 'time', 'echo_number', 'number_of_frames',
                      'acq_date', 'acq_time', 'receiving_c', 'acq_number', 'slice_location', 'samples_per',
                      'photo_metric', 'rows', 'columns', 'bits_stored', 'image_type', 'identity', 'object_file',
                      'device_name')
            ]
        ]
        inputs = [
            (CtSeries('identity 1', 'number 1', 'modality 1', 'manufacture 1', 'model_name 1',
                      'patient_position 1', 'date 1', 'time 1', 'description 1', 'body_part_ex 1',
                      'protocol_name 1', 'institution 1', 'frame_of_reference 1'),),
            (CtSeries('identity 2', 'number 2', 'modality 2', 'manufacture 2', 'model_name 2',
                      'patient_position 2', 'date 2', 'time 2', 'description 2', 'body_part_ex 2',
                      'protocol_name 2', 'institution 2', 'frame_of_reference 2'),)
        ]
        validation_methods = {
            self.database_connector.get_execute_query_called_with_parameters: [
                {
                    'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
                    'arg': {'series_id': 'identity 1'}
                },
                {
                    'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
                    'arg': {'series_id': 'identity 2'}
                },
                {
                    'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
                    'arg': {'series_id': 'identity 1'}
                },
                {
                    'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
                    'arg': {'series_id': 'identity 2'}
                }
            ]
        }
        # validation_methods = [
        #     (1, self.database_connector.get_times_execute_query_is_called),
        #     ({'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
        #       'arg': {'series_id': 'identity 1'}},
        #      self.database_connector.get_execute_query_called_with_parameter),
        #     (2, self.database_connector.get_times_execute_query_is_called),
        #     ({'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
        #       'arg': {'series_id': 'identity 2'}},
        #      self.database_connector.get_execute_query_called_with_parameter),
        #     (3, self.database_connector.get_times_execute_query_is_called),
        #     ({'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
        #       'arg': {'series_id': 'identity 1'}},
        #      self.database_connector.get_execute_query_called_with_parameter),
        #     (4, self.database_connector.get_times_execute_query_is_called),
        #     ({'sql_query': 'SELECT ObjectFile\nFROM DICOMImages\nWHERE SeriesInst = :series_id',
        #       'arg': {'series_id': 'identity 2'}},
        #      self.database_connector.get_execute_query_called_with_parameter)
        # ]
        return_value_mocked_methods = [
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1',
                        'number_of_frames 1', 'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1',
                        'slice_location 1', 'samples_per 1', 'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1',
                        'image_type 1', 'identity 1', 'object_file 1', 'device_name 1'],
                    '2': [
                        'instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2',
                        'number_of_frames 2', 'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2',
                        'slice_location 2', 'samples_per 2', 'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2',
                        'image_type 2', 'identity 2', 'object_file 2', 'device_name 2']
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1',
                        'number_of_frames 1', 'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1',
                        'slice_location 1', 'samples_per 1', 'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1',
                        'image_type 1', 'identity 1', 'object_file 1', 'device_name 1'],
                    '2': [
                        'instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2',
                        'number_of_frames 2', 'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2',
                        'slice_location 2', 'samples_per 2', 'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2',
                        'image_type 2', 'identity 2', 'object_file 2', 'device_name 2']
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance test', 'class_id test', 'number test', 'date test', 'time test', 'echo_number test',
                        'number_of_frames test', 'acq_date test', 'acq_time test', 'receiving_c test',
                        'acq_number test', 'slice_location test', 'samples_per test', 'photo_metric test', 'rows test',
                        'columns test', 'bits_stored test', 'image_type test', 'identity test', 'object_file test',
                        'device_name test'
                    ],
                    '2': [
                        'test instance', 'test class_id', 'test number', 'test date', 'test time', 'test echo_number',
                        'test number_of_frames', 'test acq_date', 'test acq_time', 'test receiving_c',
                        'test acq_number', 'test slice_location', 'test samples_per', 'test photo_metric', 'test rows',
                        'test columns', 'test bits_stored', 'test image_type', 'test identity', 'test object_file',
                        'test device_name'
                    ],
                    '3': [
                        'instance', 'class_id', 'number', 'date', 'time', 'echo_number', 'number_of_frames', 'acq_date',
                        'acq_time', 'receiving_c', 'acq_number', 'slice_location', 'samples_per', 'photo_metric',
                        'rows', 'columns', 'bits_stored', 'image_type', 'identity', 'object_file', 'device_name'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance test', 'class_id test', 'number test', 'date test', 'time test', 'echo_number test',
                        'number_of_frames test', 'acq_date test', 'acq_time test', 'receiving_c test',
                        'acq_number test', 'slice_location test', 'samples_per test', 'photo_metric test', 'rows test',
                        'columns test', 'bits_stored test', 'image_type test', 'identity test', 'object_file test',
                        'device_name test'
                    ],
                    '2': [
                        'test instance', 'test class_id', 'test number', 'test date', 'test time', 'test echo_number',
                        'test number_of_frames', 'test acq_date', 'test acq_time', 'test receiving_c',
                        'test acq_number', 'test slice_location', 'test samples_per', 'test photo_metric', 'test rows',
                        'test columns', 'test bits_stored', 'test image_type', 'test identity', 'test object_file',
                        'test device_name'
                    ],
                    '3': [
                        'instance', 'class_id', 'number', 'date', 'time', 'echo_number', 'number_of_frames', 'acq_date',
                        'acq_time', 'receiving_c', 'acq_number', 'slice_location', 'samples_per', 'photo_metric',
                        'rows', 'columns', 'bits_stored', 'image_type', 'identity', 'object_file', 'device_name'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            ))
        ]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_get_image_by_id(self):
        method_to_test = self.image_repos.get_image_by_id
        outputs = [
            Image('instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1', 'number_of_frames 1',
                  'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1', 'slice_location 1', 'samples_per 1',
                  'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1', 'image_type 1', 'identity 1',
                  'object_file 1', 'device_name 1'),
            Image('instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2', 'number_of_frames 2',
                  'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2', 'slice_location 2', 'samples_per 2',
                  'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2', 'image_type 2', 'identity 2',
                  'object_file 2', 'device_name 2')
        ]
        inputs = [('instance 1',), ('instance 2',)]
        validation_methods = [
            (1, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE SOPInstanc = :image_id',
              'arg': {'image_id': 'instance 1'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (2, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE SOPInstanc = :image_id',
              'arg': {'image_id': 'instance 2'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (3, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE SOPInstanc = :image_id',
              'arg': {'image_id': 'instance 1'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (4, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE SOPInstanc = :image_id',
              'arg': {'image_id': 'instance 2'}},
             self.database_connector.get_execute_query_called_with_parameter)
        ]
        return_value_mocked_methods = [
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1',
                        'number_of_frames 1', 'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1',
                        'slice_location 1', 'samples_per 1', 'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1',
                        'image_type 1', 'identity 1', 'object_file 1', 'device_name 1'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1',
                        'number_of_frames 1', 'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1',
                        'slice_location 1', 'samples_per 1', 'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1',
                        'image_type 1', 'identity 1', 'object_file 1', 'device_name 1'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2',
                        'number_of_frames 2', 'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2',
                        'slice_location 2', 'samples_per 2', 'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2',
                        'image_type 2', 'identity 2', 'object_file 2', 'device_name 2'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2',
                        'number_of_frames 2', 'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2',
                        'slice_location 2', 'samples_per 2', 'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2',
                        'image_type 2', 'identity 2', 'object_file 2', 'device_name 2'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            ))
        ]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_get_images_of_patients_last_ct_series_matching_return(self):
        rtstruct_image_1 = Image(
            'rtstruct image instance 1', 'rtstruct image class ui 1', 'rtstruct image number 1',
            'rtstruct image date 1', 'rtstruct image time 1', 'rtstruct image echo_number 1',
            'rtstruct image number_of_frames 1', 'rtstruct image acq_date 1', 'rtstruct image acq_time 1',
            'rtstruct image receiving_c 1', 'rtstruct image acq_number 1', 'rtstruct image slice location 1',
            'rtstruct image samples_per 1', 'rtstruct image photo_metric 1', 'rtstruct image rows 1',
            'rtstruct image columns 1', 'rtstruct image bits_stored 1', 'rtstruct image image_type 1',
            'rtstruct image identity 1', 'rtstruct image object_file 1', 'rtstruct image device_name 1')
        rtstruct_image_2 = Image(
            'rtstruct image instance 2', 'rtstruct image class ui 2', 'rtstruct image number 2',
            'rtstruct image date 2', 'rtstruct image time 2', 'rtstruct image echo_number 2',
            'rtstruct image number_of_frames 2', 'rtstruct image acq_date 2', 'rtstruct image acq_time 2',
            'rtstruct image receiving_c 2', 'rtstruct image acq_number 2', 'rtstruct image slice location 2',
            'rtstruct image samples_per 2', 'rtstruct image photo_metric 2', 'rtstruct image rows 2',
            'rtstruct image columns 2', 'rtstruct image bits_stored 2', 'rtstruct image image_type 2',
            'rtstruct image identity 2', 'rtstruct image object_file 2', 'rtstruct image device_name 2')
        rtstruct_image_3 = Image(
            'rtstruct image instance 3', 'rtstruct image class ui 3', 'rtstruct image number 3',
            'rtstruct image date 3', 'rtstruct image time 3', 'rtstruct image echo_number 3',
            'rtstruct image number_of_frames 3', 'rtstruct image acq_date 3', 'rtstruct image acq_time 3',
            'rtstruct image receiving_c 3', 'rtstruct image acq_number 3', 'rtstruct image slice location 3',
            'rtstruct image samples_per 3', 'rtstruct image photo_metric 3', 'rtstruct image rows 3',
            'rtstruct image columns 3', 'rtstruct image bits_stored 3', 'rtstruct image image_type 3',
            'rtstruct image identity 3', 'rtstruct image object_file 3', 'rtstruct image device_name 3')
        ct_image_1 = Image(
            'ct image instance 1', 'ct image class_ui 1', 'ct image number 1', 'ct image date 1', 'ct image time 1',
            'ct image echo_number 1', 'ct image number_of_frames 1', 'ct image acq_date 1', 'ct image acq_time 1',
            'ct image receiving_c 1', 'ct image acq_number 1', 'ct image slice_location 1', 'ct image samples_per',
            'ct image photo_metric 1', 'ct image rows 1', 'ct image columns 1', 'ct image bits_stored 1',
            'ct image image_type 1', 'ct image identity 1', 'ct image object_file 1', 'ct image device_name 1')
        ct_image_2 = Image(
            'ct image instance 2', 'ct image class_ui 2', 'ct image number 2', 'ct image date 2', 'ct image time 2',
            'ct image echo_number 2', 'ct image number_of_frames 2', 'ct image acq_date 2', 'ct image acq_time 2',
            'ct image receiving_c 2', 'ct image acq_number 2', 'ct image slice_location 2', 'ct image samples_per',
            'ct image photo_metric 2', 'ct image rows 2', 'ct image columns 2', 'ct image bits_stored 2',
            'ct image image_type 2', 'ct image identity 2', 'ct image object_file 2', 'ct image device_name 2')
        ct_image_3 = Image(
            'ct image instance 3', 'ct image class_ui 3', 'ct image number 3', 'ct image date 3', 'ct image time 3',
            'ct image echo_number 3', 'ct image number_of_frames 3', 'ct image acq_date 3', 'ct image acq_time 3',
            'ct image receiving_c 3', 'ct image acq_number 3', 'ct image slice_location 3', 'ct image samples_per',
            'ct image photo_metric 3', 'ct image rows 3', 'ct image columns 3', 'ct image bits_stored 3',
            'ct image image_type 3', 'ct image identity 3', 'ct image object_file 3', 'ct image device_name 3')
        ct_image_4 = Image(
            'ct image instance 4', 'ct image class_ui 4', 'ct image number 4', 'ct image date 4', 'ct image time 4',
            'ct image echo_number 4', 'ct image number_of_frames 4', 'ct image acq_date 4', 'ct image acq_time 4',
            'ct image receiving_c 4', 'ct image acq_number 4', 'ct image slice_location 4', 'ct image samples_per',
            'ct image photo_metric 4', 'ct image rows 4', 'ct image columns 4', 'ct image bits_stored 4',
            'ct image image_type 4', 'ct image identity 4', 'ct image object_file 4', 'ct image device_name 4')
        ct_image_5 = Image(
            'ct image instance 5', 'ct image class_ui 5', 'ct image number 5', 'ct image date 5', 'ct image time 5',
            'ct image echo_number 5', 'ct image number_of_frames 5', 'ct image acq_date 5', 'ct image acq_time 5',
            'ct image receiving_c 5', 'ct image acq_number 5', 'ct image slice_location 5', 'ct image samples_per',
            'ct image photo_metric 5', 'ct image rows 5', 'ct image columns 5', 'ct image bits_stored 5',
            'ct image image_type 5', 'ct image identity 5', 'ct image object_file 5', 'ct image device_name 5')
        ct_image_6 = Image(
            'ct image instance 6', 'ct image class_ui 6', 'ct image number 6', 'ct image date 6', 'ct image time 6',
            'ct image echo_number 6', 'ct image number_of_frames 6', 'ct image acq_date 6', 'ct image acq_time 6',
            'ct image receiving_c 6', 'ct image acq_number 6', 'ct image slice_location 6', 'ct image samples_per',
            'ct image photo_metric 6', 'ct image rows 6', 'ct image columns 6', 'ct image bits_stored 6',
            'ct image image_type 6', 'ct image identity 6', 'ct image object_file 6', 'ct image device_name 6')
        pet_image_1 = Image(
            'pet image instance 1', 'pet image class_ui 1', 'pet image number 1', 'pet image date 1', 'pet image time 1',
            'pet image echo_number 1', 'pet image number_of_frames 1', 'pet image acq_date 1', 'pet image acq_time 1',
            'pet image receiving_c 1', 'pet image acq_number 1', 'pet image slice_location 1', 'pet image samples_per',
            'pet image photo_metric 1', 'pet image rows 1', 'pet image columns 1', 'pet image bits_stored 1',
            'pet image image_type 1', 'pet image identity 1', 'pet image objepet_file 1', 'pet image device_name 1')
        pet_image_2 = Image(
            'pet image instance 2', 'pet image class_ui 2', 'pet image number 2', 'pet image date 2', 'pet image time 2',
            'pet image echo_number 2', 'pet image number_of_frames 2', 'pet image acq_date 2', 'pet image acq_time 2',
            'pet image receiving_c 2', 'pet image acq_number 2', 'pet image slice_location 2', 'pet image samples_per',
            'pet image photo_metric 2', 'pet image rows 2', 'pet image columns 2', 'pet image bits_stored 2',
            'pet image image_type 2', 'pet image identity 2', 'pet image objepet_file 2', 'pet image device_name 2')
        pet_image_3 = Image(
            'pet image instance 3', 'pet image class_ui 3', 'pet image number 3', 'pet image date 3', 'pet image time 3',
            'pet image echo_number 3', 'pet image number_of_frames 3', 'pet image acq_date 3', 'pet image acq_time 3',
            'pet image receiving_c 3', 'pet image acq_number 3', 'pet image slice_location 3', 'pet image samples_per',
            'pet image photo_metric 3', 'pet image rows 3', 'pet image columns 3', 'pet image bits_stored 3',
            'pet image image_type 3', 'pet image identity 3', 'pet image objepet_file 3', 'pet image device_name 3')
        pet_image_4 = Image(
            'pet image instance 4', 'pet image class_ui 4', 'pet image number 4', 'pet image date 4', 'pet image time 4',
            'pet image echo_number 4', 'pet image number_of_frames 4', 'pet image acq_date 4', 'pet image acq_time 4',
            'pet image receiving_c 4', 'pet image acq_number 4', 'pet image slice_location 4', 'pet image samples_per',
            'pet image photo_metric 4', 'pet image rows 4', 'pet image columns 4', 'pet image bits_stored 4',
            'pet image image_type 4', 'pet image identity 4', 'pet image objepet_file 4', 'pet image device_name 4')
        pet_image_5 = Image(
            'pet image instance 5', 'pet image class_ui 5', 'pet image number 5', 'pet image date 5', 'pet image time 5',
            'pet image echo_number 5', 'pet image number_of_frames 5', 'pet image acq_date 5', 'pet image acq_time 5',
            'pet image receiving_c 5', 'pet image acq_number 5', 'pet image slice_location 5', 'pet image samples_per',
            'pet image photo_metric 5', 'pet image rows 5', 'pet image columns 5', 'pet image bits_stored 5',
            'pet image image_type 5', 'pet image identity 5', 'pet image objepet_file 5', 'pet image device_name 5')
        pet_image_6 = Image(
            'pet image instance 6', 'pet image class_ui 6', 'pet image number 6', 'pet image date 6', 'pet image time 6',
            'pet image echo_number 6', 'pet image number_of_frames 6', 'pet image acq_date 6', 'pet image acq_time 6',
            'pet image receiving_c 6', 'pet image acq_number 6', 'pet image slice_location 6', 'pet image samples_per',
            'pet image photo_metric 6', 'pet image rows 6', 'pet image columns 6', 'pet image bits_stored 6',
            'pet image image_type 6', 'pet image identity 6', 'pet image objepet_file 6', 'pet image device_name 6')

        rtstruct_series_1 = RtstructSeries(
            'rtstruct identity 1', 'rtstruct number 1', 'rtstruct modality 1', 'rtstruct manufacture 1',
            'rtstruct model_name 1', 'rtstruct patient_position 1', rtstruct_image_1)

        rtstruct_series_2 = RtstructSeries(
            'rtstruct identity 2', 'rtstruct number 2', 'rtstruct modality 2', 'rtstruct manufacture 2',
            'rtstruct model_name 2', 'rtstruct patient_position 2', rtstruct_image_2)

        rtstruct_series_3 = RtstructSeries(
            'rtstruct identity 3', 'rtstruct number 3', 'rtstruct modality 3', 'rtstruct manufacture 3',
            'rtstruct model_name 3', 'rtstruct patient_position 3', rtstruct_image_3)

        ct_series_1 = CtSeries(
            'ct identity 1', 'ct number 1', 'ct modality 1', 'ct manufacture 1', 'ct model_name 1',
            'ct patient_position 1', 'ct date 1', 'ct time 1', 'ct description 1', 'ct body_part_ex 1',
            'ct protocol_name 1', 'ct institution 1', 'ct frame_of_reference 1', [ct_image_1, ct_image_2, ct_image_3])

        ct_series_2 = CtSeries(
            'ct identity 2', 'ct number 2', 'ct modality 2', 'ct manufacture 2', 'ct model_name 2',
            'ct patient_position 2', 'ct date 2', 'ct time 2', 'ct description 2', 'ct body_part_ex 2',
            'ct protocol_name 2', 'ct institution 2', 'ct frame_of_reference 2', [ct_image_4, ct_image_5, ct_image_6])

        ct_series_3 = CtSeries(
            'ct identity 3', 'ct number 3', 'ct modality 3', 'ct manufacture 3', 'ct model_name 3',
            'ct patient_position 3', 'ct date 3', 'ct time 3', 'ct description 3', 'ct body_part_ex 3',
            'ct protocol_name 3', 'ct institution 3', 'ct frame_of_reference 3',
            [ct_image_1, ct_image_2, ct_image_3, ct_image_4, ct_image_5, ct_image_6])

        pet_series_1 = PetSeries(
            'pet identity 1', 'pet number 1', 'pet modality 1', 'pet manufacture 1', 'pet model_name 1',
            'pet patient_position 1', 'pet date 1', 'pet time 1', 'pet description 1', 'pet body_part_ex 1',
            'pet protocol_name 1', 'pet institution 1', 'pet frame_of_reference 1',
            [pet_image_1, pet_image_2, pet_image_3])

        pet_series_2 = PetSeries(
            'pet identity 2', 'pet number 2', 'pet modality 2', 'pet manufacture 2', 'pet model_name 2',
            'pet patient_position 2', 'pet date 2', 'pet time 2', 'pet description 2', 'pet body_part_ex 2',
            'pet protocol_name 2', 'pet institution 2', 'pet frame_of_reference 2',
            [pet_image_4, pet_image_5, pet_image_6])

        pet_series_3 = PetSeries(
            'pet identity 3', 'pet number 3', 'pet modality 3', 'pet manufacture 3', 'pet model_name 3',
            'pet patient_position 3', 'pet date 3', 'pet time 3', 'pet description 3', 'pet body_part_ex 3',
            'pet protocol_name 3', 'pet institution 3', 'pet frame_of_reference 3',
            [pet_image_1, pet_image_2, pet_image_3, pet_image_4, pet_image_5, pet_image_6])

        study_1 = Study(
            'study instance 1', 'date 1', 'time 1', 'identity 1', 'description 1', 'accession_n 1', 'refer_physicist 1',
            'patients_ag 1', 'patient_we 1', 'modalities 1', [rtstruct_series_1, ct_series_1])

        study_2 = Study(
            'study instance 2', 'date 2', 'time 2', 'identity 2', 'description 2', 'accession_n 2', 'refer_physicist 2',
            'patients_ag 2', 'patient_we 2', 'modalities 2', [rtstruct_series_2, ct_series_2])

        study_3 = Study(
            'study instance 3', 'date 3', 'time 3', 'identity 3', 'description 3', 'accession_n 3', 'refer_physicist 3',
            'patients_ag 3', 'patient_we 3', 'modalities 3', [rtstruct_series_3, ct_series_3])

        study_4 = Study(
            'study instance 4', 'date 4', 'time 4', 'identity 4', 'description 4', 'accession_n 4', 'refer_physicist 4',
            'patients_ag 4', 'patient_we 4', 'modalities 4', [rtstruct_series_1, pet_series_1])

        study_5 = Study(
            'study instance 5', 'date 5', 'time 5', 'identity 5', 'description 5', 'accession_n 5', 'refer_physicist 5',
            'patients_ag 5', 'patient_we 5', 'modalities 5', [rtstruct_series_2, pet_series_2])

        study_6 = Study(
            'study instance 6', 'date 6', 'time 6', 'identity 6', 'description 6', 'accession_n 6', 'refer_physicist 6',
            'patients_ag 6', 'patient_we 6', 'modalities 6', [rtstruct_series_3, pet_series_3])

        study_7 = Study(
            'study instance 7', 'date 7', 'time 7', 'identity 7', 'description 7', 'accession_n 7', 'refer_physicist 7',
            'patients_ag 7', 'patient_we 7', 'modalities 7', [rtstruct_series_1, ct_series_1, ct_series_2, ct_series_3])

        study_8 = Study(
            'study instance 8', 'date 8', 'time 8', 'identity 8', 'description 8', 'accession_n 8', 'refer_physicist 8',
            'patients_ag 8', 'patient_we 8', 'modalities 8',
            [rtstruct_series_2, pet_series_1, pet_series_2, pet_series_3])

        study_9 = Study(
            'study instance 9', 'date 9', 'time 9', 'identity 9', 'description 8', 'accession_n 8', 'refer_physicist 8',
            'patients_ag 8', 'patient_we 8', 'modalities 8',
            [rtstruct_series_3, ct_series_1, ct_series_2, ct_series_3, pet_series_1, pet_series_2, pet_series_3])

        study_10 = Study(
            'study instance 10', 'date 10', 'time 10', 'identity 10', 'description 10', 'accession_n 10',
            'refer_physicist 10', 'patients_ag 10', 'patient_we 10', 'modalities 10',
            [rtstruct_series_1, rtstruct_series_2, rtstruct_series_3,
             ct_series_1, ct_series_2, ct_series_3,
             pet_series_1, pet_series_2, pet_series_3])

        patient_1 = Patient('patient identity 1', 'name 1', 'sex 1', 'access_time 1', [study_1])

        patient_2 = Patient('patient identity 2', 'name 2', 'sex 2', 'access_time 2', [study_2])

        patient_3 = Patient('patient identity 3', 'name 3', 'sex 3', 'access_time 3', [study_3])

        patient_4 = Patient('patient identity 4', 'name 4', 'sex 4', 'access_time 4', [study_4])

        patient_5 = Patient('patient identity 5', 'name 5', 'sex 5', 'access_time 5', [study_5])

        patient_6 = Patient('patient identity 6', 'name 6', 'sex 6', 'access_time 6', [study_6])

        patient_7 = Patient('patient identity 7', 'name 7', 'sex 7', 'access_time 7', [study_7])

        patient_8 = Patient('patient identity 8', 'name 8', 'sex 8', 'access_time 8', [study_8])

        patient_9 = Patient('patient identity 9', 'name 9', 'sex 9', 'access_time 9', [study_9])

        patient_10 = Patient('patient identity 10', 'name 10', 'sex 10', 'access_time 10', [study_10])

        patient_11 = Patient('patient identity 11', 'name 11', 'sex 11', 'access_time 11', [study_1, study_2, study_3])

        patient_12 = Patient('patient identity 12', 'name 12', 'sex 12', 'access_time 12', [study_4, study_5, study_6])

        patient_13 = Patient('patient identity 13', 'name 13', 'sex 13', 'access_time 13', [study_1, study_5])

        patient_14 = Patient('patient identity 14', 'name 14', 'sex 14', 'access_time 14', [study_1, study_6])

        patient_15 = Patient('patient identity 15', 'name 15', 'sex 15', 'access_time 15', [study_2, study_4])

        patient_16 = Patient('patient identity 16', 'name 16', 'sex 16', 'access_time 16', [study_2, study_6])

        patient_17 = Patient('patient identity 17', 'name 17', 'sex 17', 'access_time 17', [study_3, study_4])

        patient_18 = Patient('patient identity 18', 'name 18', 'sex 18', 'access_time 18', [study_3, study_5])

        method_to_test = self.image_repos.get_images_of_patients_last_ct_series_matching_rtstruct
        outputs = [
            [
                (patient_1, rtstruct_series_1, ct_series_1)
            ],
            [
                (patient_2, rtstruct_series_2, ct_series_2)
            ],
            [
                (patient_3, rtstruct_series_3, ct_series_3)
            ],
            [
                (patient_4, rtstruct_series_1, pet_series_1)
            ],
            [
                (patient_5, rtstruct_series_2, pet_series_2)
            ],
            [
                (patient_6, rtstruct_series_3, pet_series_3)
            ],
            [
                (patient_7, rtstruct_series_1, ct_series_1),
                (patient_7, rtstruct_series_1, ct_series_2),
                (patient_7, rtstruct_series_1, ct_series_3)
            ],
            [
                (patient_8, rtstruct_series_2, pet_series_1),
                (patient_8, rtstruct_series_2, pet_series_2),
                (patient_8, rtstruct_series_2, pet_series_3)
            ],
            [
                (patient_9, rtstruct_series_3, ct_series_1),
                (patient_9, rtstruct_series_3, ct_series_2),
                (patient_9, rtstruct_series_3, ct_series_3),
                (patient_9, rtstruct_series_3, pet_series_1),
                (patient_9, rtstruct_series_3, pet_series_2),
                (patient_9, rtstruct_series_3, pet_series_3)
            ],
            [
                (patient_10, rtstruct_series_1, ct_series_1),
                (patient_10, rtstruct_series_1, ct_series_2),
                (patient_10, rtstruct_series_1, ct_series_3),
                (patient_10, rtstruct_series_1, pet_series_1),
                (patient_10, rtstruct_series_1, pet_series_2),
                (patient_10, rtstruct_series_1, pet_series_3),
                (patient_10, rtstruct_series_2, ct_series_1),
                (patient_10, rtstruct_series_2, ct_series_2),
                (patient_10, rtstruct_series_2, ct_series_3),
                (patient_10, rtstruct_series_2, pet_series_1),
                (patient_10, rtstruct_series_2, pet_series_2),
                (patient_10, rtstruct_series_2, pet_series_3),
                (patient_10, rtstruct_series_3, ct_series_1),
                (patient_10, rtstruct_series_3, ct_series_2),
                (patient_10, rtstruct_series_3, ct_series_3),
                (patient_10, rtstruct_series_3, pet_series_1),
                (patient_10, rtstruct_series_3, pet_series_2),
                (patient_10, rtstruct_series_3, pet_series_3)
            ],
            [
                (patient_11, rtstruct_series_1, ct_series_1),
                (patient_11, rtstruct_series_2, ct_series_2),
                (patient_11, rtstruct_series_3, ct_series_3)
            ],
            [
                (patient_12, rtstruct_series_1, pet_series_1),
                (patient_12, rtstruct_series_2, pet_series_2),
                (patient_12, rtstruct_series_3, pet_series_3)
            ],
            [
                (patient_13, rtstruct_series_1, ct_series_1),
                (patient_13, rtstruct_series_2, pet_series_2)
            ],
            [
                (patient_14, rtstruct_series_1, ct_series_1),
                (patient_14, rtstruct_series_3, pet_series_3)
            ],
            [
                (patient_15, rtstruct_series_2, ct_series_2),
                (patient_15, rtstruct_series_1, pet_series_1)
            ],
            [
                (patient_16, rtstruct_series_2, ct_series_2),
                (patient_16, rtstruct_series_3, pet_series_3)
            ],
            [
                (patient_17, rtstruct_series_3, ct_series_3),
                (patient_17, rtstruct_series_1, pet_series_1)
            ],
            [
                (patient_18, rtstruct_series_3, ct_series_3),
                (patient_18, rtstruct_series_2, pet_series_2)
            ]
        ]
        inputs = [('instance 1',), ('instance 2',)]
        validation_methods = [
            (1, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': "SELECT ImageRtstruct.ImagePat AS 'patient_id', SeriesRtstruct.StudyInsta AS 'study_id',\n"
                           "\tImageRtstruct.SeriesInst AS 'rtstruct_series_id',"
                           " ImageRtstruct.ObjectFile AS 'rtstruct_file',\n"
                           "\tSeriesOfImageSlices.SeriesInst AS 'series_of_slices_id',"
                           " ImageSlices.ObjectFile AS 'image_slice_id'\n"
                           "FROM DICOMImages ImageRtstruct, DICOMSeries SeriesRtstruct,"
                           " DICOMSeries SeriesofImageSlices, DICOMImages ImageSlices\n"
                           "WHERE ImageRtstruct.SOPInstanc = :image_id AND"
                           " (SeriesofImageSlices.Modality = 'CT' OR SeriesofImageSlices.Modality = 'PT')\n"
                           "\tAND ImageRtstruct.SeriesInst = SeriesRtstruct.SeriesInst\n"
                           "\tAND SeriesofImageSlices.StudyInsta = SeriesRtstruct.StudyInsta"
                           " AND ImageSlices.SeriesInst = SeriesofImageSlices.SeriesInst\n"
                           "ORDER BY ImageRtstruct.ImagePat, SeriesRtstruct.StudyInsta,"
                           " ImageRtstruct.SeriesInst, SeriesofImageSlices.SeriesInst,\n"
                           "CAST(ImageSlices.ImageNumbe AS INTEGER)",
              'arg': {'image_id': 'instance 1'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (2, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'ct image object_file 1'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (3, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'ct image object_file 2'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (4, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'ct image object_file 3'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (5, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'rtstruct image object_file 1'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (1, self.series_repos.get_times_get_series_from_id_is_called),
            ('rtstruct identity 1', self.series_repos.get_get_series_from_id_called_with_parameter),
            (2, self.series_repos.get_times_get_series_from_id_is_called),
            ('ct identity 1', self.series_repos.get_get_series_from_id_called_with_parameter),
            (3, self.series_repos)
        ]
        return_value_mocked_methods = [

        ]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)

    def test_get_image_by_file_path(self):
        method_to_test = self.image_repos.get_image_by_file_path
        outputs = [
            Image('instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1', 'number_of_frames 1',
                  'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1', 'slice_location 1', 'samples_per 1',
                  'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1', 'image_type 1', 'identity 1',
                  'object_file 1', 'device_name 1'),
            Image('instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2', 'number_of_frames 2',
                  'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2', 'slice_location 2', 'samples_per 2',
                  'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2', 'image_type 2', 'identity 2',
                  'object_file 2', 'device_name 2')
        ]
        inputs = [('object_file 1',), ('object_file 2',)]
        validation_methods = [
            (1, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'object_file 1'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (2, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'object_file 2'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (3, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'object_file 1'}},
             self.database_connector.get_execute_query_called_with_parameter),
            (4, self.database_connector.get_times_execute_query_is_called),
            ({'sql_query': 'SELECT *\nFROM DICOMImages\nWHERE ObjectFile = :object_file',
              'arg': {'object_file': 'object_file 2'}},
             self.database_connector.get_execute_query_called_with_parameter)
        ]
        return_value_mocked_methods = [
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1',
                        'number_of_frames 1', 'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1',
                        'slice_location 1', 'samples_per 1', 'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1',
                        'image_type 1', 'identity 1', 'object_file 1', 'device_name 1'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 1', 'class_id 1', 'number 1', 'date 1', 'time 1', 'echo_number 1',
                        'number_of_frames 1', 'acq_date 1', 'acq_time 1', 'receiving_c 1', 'acq_number 1',
                        'slice_location 1', 'samples_per 1', 'photo_metric 1', 'rows 1', 'columns 1', 'bits_stored 1',
                        'image_type 1', 'identity 1', 'object_file 1', 'device_name 1'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2',
                        'number_of_frames 2', 'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2',
                        'slice_location 2', 'samples_per 2', 'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2',
                        'image_type 2', 'identity 2', 'object_file 2', 'device_name 2'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            )),
            (self.database_connector.set_execute_query_result_value, pd.DataFrame.from_dict(
                {
                    '1': [
                        'instance 2', 'class_id 2', 'number 2', 'date 2', 'time 2', 'echo_number 2',
                        'number_of_frames 2', 'acq_date 2', 'acq_time 2', 'receiving_c 2', 'acq_number 2',
                        'slice_location 2', 'samples_per 2', 'photo_metric 2', 'rows 2', 'columns 2', 'bits_stored 2',
                        'image_type 2', 'identity 2', 'object_file 2', 'device_name 2'
                    ]
                }, orient='index', columns=[
                    'SOPInstanc', 'SOPClassUI', 'ImageNumbe', 'ImageDate', 'ImageTime', 'EchoNumber', 'NumberOfFr',
                    'AcqDate', 'AcqTime', 'ReceivingC', 'AcqNumber', 'SliceLocat', 'SamplesPer', 'PhotoMetri', 'Rows',
                    'Colums', 'BitsStored', 'ImageType', 'ImageID', 'ObjectFile', 'DeviceName'
                ]
            ))
        ]

        self.load_test_setup(method_to_test, outputs, inputs, validation_methods, return_value_mocked_methods)
