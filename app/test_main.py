import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@1",
    "Pa$$w0rd123456789"
])
def test_length(password: str) -> None:
    assert not check_password(password)


def test_missing_uppercase() -> None:
    assert not check_password("pass@word1")


def test_missing_digit() -> None:
    assert not check_password("Password@")


def test_missing_special() -> None:
    assert not check_password("Password1")


def test_invalid_character() -> None:
    assert not check_password("Pass?word1")


def test_valid_password() -> None:
    assert check_password("Pass@word1")
