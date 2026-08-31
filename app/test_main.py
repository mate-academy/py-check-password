
from app.main import check_password


def test_should_check_min_length() -> None:
    assert check_password("Ab@12") is False, "too short"


def test_should_check_max_length() -> None:
    assert check_password("A" * 17 + "@1") is False, "too long"


def test_should_check_digit() -> None:
    assert check_password("Password@") is False, "no digits"


def test_should_check_special_symbols() -> None:
    assert check_password("Password1") is False, "no special symbols"


def test_should_check_upper_letter() -> None:
    assert check_password("password1@") is False, "no upper letters"


def test_should_check_valid_value() -> None:
    assert check_password("Pass@word1") is True, "password is valid"
