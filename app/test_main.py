from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_invalid_min_length() -> None:
    assert check_password("P@ss1") is False


def test_invalid_max_length() -> None:
    assert check_password("Pass@worddd1312311") is False


def test_invalid_upper_letter() -> None:
    assert check_password("pass@word123") is False


def test_invalid_digits() -> None:
    assert check_password("Pass@worddd") is False


def test_invalid_special_char() -> None:
    assert check_password("Password123456") is False
