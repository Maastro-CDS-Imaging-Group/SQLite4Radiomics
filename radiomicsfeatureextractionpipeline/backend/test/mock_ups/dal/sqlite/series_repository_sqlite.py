from dal.sqlite.series_repository_sqlite import SeriesRepositorySqlite
from test.mock_ups.dal.series_repository import SeriesRepositoryMockUp


class SeriesRepositorySqliteMockUp(SeriesRepositorySqlite, SeriesRepositoryMockUp):
    pass
