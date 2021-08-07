import pytest

from tests.testdata import (
    VALID_BEAR_TYPES,
    INVALID_BEAR_TYPES,
    INVALID_BEAR_AGES,
    INVALID_BEAR_NAMES,
)


class TestPostApi:
    @pytest.mark.parametrize("type_", VALID_BEAR_TYPES)
    def test_create_available_type(self, api, type_):
        data = {"bear_type": type_, "bear_name": type_.lower(), "bear_age": 42}
        response = api.create_bear(data)
        assert response.status_code == 200
        id_ = response.json()

        bear = api.get_bear(id_).json()
        assert isinstance(bear, dict)
        assert bear["bear_type"] == type_
        assert bear["bear_name"] == type_
        assert bear["bear_age"] == 42

    @pytest.mark.parametrize("type_", INVALID_BEAR_TYPES)
    def test_create_invalid_type(self, api, type_):
        data = {"bear_type": type_, "bear_name": "BEAR_WITH_INVALID_TYPE", "bear_age": 42}
        response = api.create_bear(data)
        assert response.status_code == 500

    @pytest.mark.parametrize("name", INVALID_BEAR_NAMES)
    def test_create_invalid_name(self, api, name):
        data = {"bear_type": "POLAR", "bear_name": name, "bear_age": 42}
        response = api.create_bear(data)
        assert response.status_code == 500

    @pytest.mark.parametrize("age", INVALID_BEAR_AGES)
    def test_create_invalid_age(self, api, age):
        data = {"bear_type": "POLAR", "bear_name": "BEAR_WITH_INVALID_AGE", "bear_age": age}
        response = api.create_bear(data)
        assert response.status_code == 500
