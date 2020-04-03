from dal.sqlite.patient_repository_sqlite import PatientRepositorySqlite
from test.mock_ups.dal.patient_repository import PatientRepositoryMockUp

class PatientRepositorySqliteMockUp(PatientRepositorySqlite, PatientRepositoryMockUp):
    pass