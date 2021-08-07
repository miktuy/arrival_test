from http import HTTPStatus

from tests.misc import check_bear
from tests.testdata import FIRST_VALID_BEAR, SECOND_VALID_BEAR


class TestGetApi:
    def test_get_all_bears_when_bears_not_exist(self, api):
        response = api.get_all_bears()
        assert response.status_code == HTTPStatus.OK
        assert len(response.json()) == 0

    def test_get_all_bears_when_one_exists(self, api, create_test_bear):
        response = api.get_all_bears()
        assert response.status_code == HTTPStatus.OK
        data = response.json()[0]
        check_bear(expected_bear=FIRST_VALID_BEAR, bear=data)

    def test_get_all_bears_when_several_exist(self, api, create_several_bears):
        response = api.get_all_bears()
        assert response.status_code == HTTPStatus.OK
        assert len(response.json()) == 2
        check_bear(FIRST_VALID_BEAR, response.json()[0])
        check_bear(SECOND_VALID_BEAR, response.json()[1])

    def test_get_bear_by_id(self, api, create_several_bears):
        id_ = create_several_bears[1]
        response = api.get_bear(id_)
        assert response.status_code == HTTPStatus.OK
        data = response.json()
        assert data["bear_id"] == id_
        check_bear(expected_bear=SECOND_VALID_BEAR, bear=data)

    def test_get_bear_by_not_exists_id(self, api, create_test_bear):
        id_ = create_test_bear
        response = api.get_bear(id_ + 1)
        assert response.status_code == HTTPStatus.OK
        assert response.text == "EMPTY"

    def test_get_bear_without_id(self, api):
        response = api.get_bear("")
        assert response.status_code == HTTPStatus.NOT_FOUND

    def test_get_bear_by_invalid_id(self, api):
        response = api.get_bear("ONE_HUNDRED_PERCENT_THIS_IS_NOT_ID")
        assert response.status_code == HTTPStatus.OK
        assert response.text == "EMPTY"
