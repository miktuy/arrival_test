import pytest


available_types = ['POLAR', 'BROWN', 'BLACK', 'GUMMY']


@pytest.mark.parametrize("type_", available_types, bears, clean_data)
def test_create_available_types(type_: str, available_types, bears, clean_data):
    data = {'bear_type': type_, 'bear_name': type_.lower(), 'bear_age': 42}
    response = bears().create_bear()
    assert response.status_code == 200

    body = bears().get_bears().json()[0]
    assert body['bear_type'] == type_
    assert body['bear_name'] == type_.lower()
    assert body['bear_age'] == 42
