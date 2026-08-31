from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True,\
        "Valid password should return True"


def test_short_password() -> None:
    assert check_password("Short1!") is False,\
        "Password shorter than 8 characters should return False"


def test_long_password() -> None:
    assert check_password("ThisPasswordIsWayTooLong123@") is False,\
        "Password longer than 16 characters should return False"


def test_missing_uppercase() -> None:
    assert check_password("password1@") is False,\
        "Password without an uppercase letter should return False"


def test_missing_digit() -> None:
    assert check_password("Password@") is False,\
        "Password without a digit should return False"


def test_missing_special_character() -> None:
    assert check_password("Password1") is False,\
        "Password without a special character should return False"


def test_invalid_character() -> None:
    assert check_password("Password1$%") is False,\
        "Password with invalid characters should return False"


def test_valid_edge_case_8_chars() -> None:
    assert check_password("A1@a1@a1") is True, \
        "Password with 8 valid characters should return True"


def test_valid_edge_case_16_chars() -> None:
    assert check_password("ValidPass1@_-!") is True,\
        "Password with 16 valid characters should return True"
