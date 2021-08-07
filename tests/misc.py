def check_bear(expected_bear: dict, bear: dict):
    assert bear["bear_type"] == expected_bear["bear_type"]
    assert bear["bear_name"] == expected_bear["bear_name"]
    assert bear["bear_age"] == expected_bear["bear_age"]