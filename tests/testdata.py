VALID_BEAR_TYPES = ["POLAR", "BROWN", "BLACK", "GUMMY"]
INVALID_BEAR_TYPES = ['', None, True, 1, 'a']
INVALID_BEAR_TYPES.extend(type_.lower() for type_ in VALID_BEAR_TYPES)

INVALID_BEAR_AGES = ['', None, True, -0.1, 'a']
INVALID_BEAR_NAMES = ['', None, True, -0.1]

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

BEAR_NEW_FULL_DATA = {
    "bear_type": "POLAR",
    "bear_name": "NEW_BEAR_NAME",
    "bear_age": 25.7,
}


BEAR_WITH_NEW_NAME = FIRST_VALID_BEAR.copy()
BEAR_WITH_NEW_NAME.update({"bear_name": "NEW_BEAR_NAME"})

BEAR_WITH_NEW_AGE = FIRST_VALID_BEAR.copy()
BEAR_WITH_NEW_AGE.update({"bear_age": 25.7})