import pytest

from app.main import check_password


@pytest.fixture()
def password() -> str:
    return "Pass@word1"


def test_check_password_with_valid_password(password: str) -> None:
    assert check_password(password)


def test_check_password_with_special_symbols(password: str) -> None:
    password = "Password1"
    assert not check_password(password)


def test_check_password_with_min_length(password: str) -> None:
    password = "Pass@1"
    assert not check_password(password)


def test_check_password_with_max_length(password: str) -> None:
    password = "Pass@word1Pass@word1"
    assert not check_password(password)


def test_check_password_with_out_digits(password: str) -> None:
    password = "Pass@word"
    assert not check_password(password)


def test_check_password_with_out_uppercase(password: str) -> None:
    password = "pass@word1"
    assert not check_password(password)
