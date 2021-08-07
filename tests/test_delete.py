from http import HTTPStatus


class TestDeleteApi:
    def test_delete_all_when_bears_not_exist(self, api):
        response = api.delete_all_bears()
        assert response.status_code == HTTPStatus.OK

    def test_delete_all_bears_when_several_bears_exist(self, api, create_several_bears):
        response = api.delete_all_bears()
        assert response.status_code == HTTPStatus.OK
        assert len(api.get_all_bears().json()) == 0

    def test_delete_exists_bear_by_id(self, api, create_several_bears):
        id_ = create_several_bears[1]
        assert len(api.get_all_bears().json()) == 2
        response = api.delete_bear(id_)
        assert response.status_code == HTTPStatus.OK
        assert len(api.get_all_bears().json()) == 1
        assert api.get_bear(id_).text == "EMPTY"

    def test_delete_bear_without_id(self, api, create_several_bears):
        response = api.delete_bear('')
        assert response.status_code == HTTPStatus.NOT_FOUND
        assert len(api.get_all_bears().json()) == 2

    def test_delete_bear_by_invalid_id(self, api, create_several_bears):
        response = api.delete_bear('ONE_HUNDRED_PERCENT_THIS_IS_NOT_ID')
        assert response.status_code == HTTPStatus.OK
        assert len(api.get_all_bears().json()) == 2

    def test_delete_bear_by_id_twice(self, api, create_several_bears):
        id_ = create_several_bears[1]
        api.delete_bear(id_)
        response = api.delete_bear(id_)
        assert response.status_code == HTTPStatus.OK
        assert len(api.get_all_bears().json()) == 1
        assert api.get_bear(id_).text == "EMPTY"
