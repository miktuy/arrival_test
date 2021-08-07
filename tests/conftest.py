import pytest

from api.bears_api import Bears
from tests.testdata import FIRST_VALID_BEAR, SECOND_VALID_BEAR
from variables import APP_HOST, APP_PORT


bears_api = Bears(host=APP_HOST, port=APP_PORT)


def _clean_data():
    bears_api.delete_all_bears()
    assert len(bears_api.get_all_bears().json()) == 0


@pytest.fixture
def api():
    return bears_api


@pytest.fixture(autouse=True)
def cleanup():
    _clean_data()
    yield
    _clean_data()


@pytest.fixture
def create_test_bear():
    return bears_api.create_bear(FIRST_VALID_BEAR).json()


@pytest.fixture
def create_several_bears():
    bear1_id = bears_api.create_bear(FIRST_VALID_BEAR).json()
    bear2_id = bears_api.create_bear(SECOND_VALID_BEAR).json()
    return [bear1_id, bear2_id]
