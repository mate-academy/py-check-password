from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_password_too_short() -> None:
    assert check_password("1234567") is False


def test_password_too_long() -> None:
    assert check_password("abcdefghijklmnopq") is False


def test_missing_uppercase() -> None:
    assert check_password("pass@word1") is False


def test_missing_digit() -> None:
    assert check_password("Password!") is False


def test_missing_special_character() -> None:
    assert check_password("Password1") is False


def test_valid_minimum_length() -> None:
    assert check_password("Aa1$ffff") is True


def test_valid_maximum_length() -> None:
    assert check_password("AbC1234$@#&-_") is True


def test_invalid_character() -> None:
    assert check_password("Pa$$wórd1") is False


def test_valid_with_all_special_characters() -> None:
    assert check_password("Pa$$w@rd1") is True


def test_invalid_with_all_special_characters() -> None:
    assert check_password("Pa$$w@rd") is False
