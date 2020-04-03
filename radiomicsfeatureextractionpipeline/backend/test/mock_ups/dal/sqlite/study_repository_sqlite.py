from dal.sqlite.study_repository_sqlite import StudyRepositorySqlite
from test.mock_ups.dal.study_repository import StudyRepositoryMockUp


class StudyRepositorySqliteMockUp(StudyRepositorySqlite, StudyRepositoryMockUp):
    pass