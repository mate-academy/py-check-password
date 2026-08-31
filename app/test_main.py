from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("St1@ng") is False


def test_no_special_character() -> None:
    assert check_password("Password1") is False


def test_no_digit() -> None:
    assert check_password("Password@") is False


def test_no_uppercase() -> None:
    assert check_password("passowrd1@") is False


def test_invalid_character() -> None:
    assert check_password("Password1!%") is False


def test_min_length_password() -> None:
    assert check_password("Abcdefg1@") is True


def test_max_length_password() -> None:
    assert check_password("Abcdefghijklm1@") is True


def test_too_long_password() -> None:
    assert check_password("Abcdefghijk0lmnop1@") is False
