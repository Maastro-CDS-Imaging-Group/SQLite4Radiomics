from logic.entities.pet_series import PetSeries
from test.mock_ups.logic.entities.series_with_image_slices import SeriesWithImageSlicesMockUp


class PetSeriesMockUp(PetSeries, SeriesWithImageSlicesMockUp):
    pass
