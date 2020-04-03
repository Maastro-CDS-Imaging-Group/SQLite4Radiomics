from logic.dicom_file_reader.basic_dicom_file_reader import BasicDicomFileReader
from test.mock_ups.logic.dicom_file_reader.dicom_file_reader import DicomFileReaderMockUp


class BasicDicomFileReaderMockUp(BasicDicomFileReader, DicomFileReaderMockUp):
    pass