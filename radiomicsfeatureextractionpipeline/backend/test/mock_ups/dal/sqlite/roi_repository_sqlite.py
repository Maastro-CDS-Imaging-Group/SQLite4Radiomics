from dal.sqlite.roi_repository_sqlite import ROIRepositorySqlite
from test.mock_ups.dal.roi_repository import ROIRepositoryMockUp


class ROIRepositorySqliteMockUp(ROIRepositorySqlite, ROIRepositoryMockUp):
    pass