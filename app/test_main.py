import pytest


from app.main import check_password


@pytest.mark.parametrize("password, result", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("1234567", False),
    ("P@ssword1998", True),
])
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result


def test_should_check_min_length() -> None:
    assert check_password("P@ss1") is False


def test_should_check_max_length() -> None:
    assert check_password("A1@superlongpassword") is False


def test_should_check_special_symbols() -> None:
    assert check_password("Password12") is False


def test_should_check_upper_letter() -> None:
    assert check_password("p@ssword12") is False


def test_should_check_digits() -> None:
    assert check_password("P@ssword") is False
