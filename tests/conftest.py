import pytest

from api.bears_api import Bears
from variables import APP_HOST, APP_PORT


FIRST_VALID_BEAR = {
    "bear_type": "BLACK",
    "bear_name": "VALID_BEAR",
    "bear_age": 42.0,
}
SECOND_VALID_BEAR = {
    "bear_type": "POLAR",
    "bear_name": "VALID BEAR",
    "bear_age": 24.0,
}


class BaseTest:
    bears_api = Bears(host=APP_HOST, port=APP_PORT)

    def _clean_data(self):
        self.bears_api.delete_all_bears()
        assert len(self.bears_api.get_all_bears().json()) == 0

    @pytest.fixture
    def setup(self):
        self._clean_data()
        yield self.bears_api
        self._clean_data()

    @pytest.fixture
    def create_test_bear(self):
        self.bears_api.create_bear(FIRST_VALID_BEAR)

    @pytest.fixture
    def create_several_bears(self):
        self.bears_api.create_bear(FIRST_VALID_BEAR)
        self.bears_api.create_bear(SECOND_VALID_BEAR)



@pytest.fixture(scope="session")
def bears():
    return bears_api
