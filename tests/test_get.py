from http import HTTPStatus
from tests.conftest import BaseTest, FIRST_VALID_BEAR


class TestGetApi(BaseTest):
    def test_get_all_bears_when_bears_not_exist(self, setup):
        api = setup
        response = api.get_all_bears()
        assert response.status_code == HTTPStatus.OK
        assert len(response.json()) == 0

    def test_get_all_bears_when_one_exists(
        self, setup, create_test_bear
    ):
        api = setup
        response = api.get_all_bears()
        assert response.status_code == HTTPStatus.OK
        assert len(response.json()) == 1
        data = response.json()[0]
        # assert data['bear_id'] == 1  TODO: delete doesn't reset `id` to 0
        assert data['bear_type'] == FIRST_VALID_BEAR['bear_type']
        assert data['bear_name'] == FIRST_VALID_BEAR['bear_name']
        assert data['bear_age'] == FIRST_VALID_BEAR['bear_age']

    def test_get_all_bears_when_several_exist(self, setup, create_several_bears):
        api = setup
        response = api.get_all_bears()
        assert response.status_code == HTTPStatus.OK
        assert len(response.json()) == 2