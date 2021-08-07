from http import HTTPStatus

import pytest

from tests.misc import check_bear
from tests.testdata import (
    VALID_BEAR_TYPES,
    INVALID_BEAR_TYPES,
    BEAR_NEW_FULL_DATA,
    BEAR_WITH_NEW_NAME,
    BEAR_WITH_NEW_AGE,
    FIRST_VALID_BEAR,
    INVALID_BEAR_AGES,
    INVALID_BEAR_NAMES,
)


class TestPositivePutApi:
    @pytest.mark.parametrize(
        "new_type", VALID_BEAR_TYPES
    )
    def test_update_bear_type(self, api, create_test_bear, new_type):
        id_ = create_test_bear
        response = api.update_bear(id_, {"bear_type": new_type})
        assert response.status_code == HTTPStatus.OK
        bear = api.get_bear(id_).json()
        assert bear["bear_id"] == id_

        bear_new_type = FIRST_VALID_BEAR.copy()
        bear_new_type.update({"bear_type": new_type})
        check_bear(bear_new_type, bear)

    def test_update_bear_name(self, api, create_test_bear):
        id_ = create_test_bear
        response = api.update_bear(id_, {"bear_name": "NEW_BEAR_NAME"})
        assert response.status_code == HTTPStatus.OK
        bear = api.get_bear(id_).json()
        assert bear["bear_id"] == id_
        check_bear(BEAR_WITH_NEW_NAME, bear)

    def test_update_bear_age(self, api, create_test_bear):
        id_ = create_test_bear
        response = api.update_bear(id_, {"bear_age": 25.7})
        assert response.status_code == HTTPStatus.OK
        bear = api.get_bear(id_).json()
        assert bear["bear_id"] == id_
        check_bear(BEAR_WITH_NEW_AGE, bear)

    def test_full_bear_update(self, api, create_test_bear):
        id_ = create_test_bear
        response = api.update_bear(id_, BEAR_NEW_FULL_DATA)
        assert response.status_code == HTTPStatus.OK
        bear = api.get_bear(id_).json()
        assert bear["bear_id"] == id_
        check_bear(BEAR_NEW_FULL_DATA, bear)


class TestNegativePutChange:

    @pytest.mark.parametrize(
        "new_type", INVALID_BEAR_TYPES
    )
    def test_set_invalid_type(self, api, create_test_bear, new_type):
        id_ = create_test_bear
        response = api.update_bear(id_, {"bear_type": new_type})
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  # TODO: change expected status code

    @pytest.mark.parametrize(
        "new_age", INVALID_BEAR_AGES
    )
    def test_set_invalid_age(self, api, create_test_bear, new_age):
        id_ = create_test_bear
        response = api.update_bear(id_, {"bear_age": new_age})
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  # TODO: change expected status code

    @pytest.mark.parametrize(
        "new_name", INVALID_BEAR_NAMES
    )
    def test_set_invalid_name(self, api, create_test_bear, new_name):
        id_ = create_test_bear
        response = api.update_bear(id_, {"bear_name": new_name})
        assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR  # TODO: change expected status code
