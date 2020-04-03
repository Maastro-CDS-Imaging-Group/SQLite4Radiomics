from dal.sqlite.image_repository_sqlite import ImageRepositorySqlite
from test.mock_ups.dal.image_repository import ImageRepositoryMockUp


class ImageRepositorySqliteMockUp(ImageRepositorySqlite, ImageRepositoryMockUp):
    pass