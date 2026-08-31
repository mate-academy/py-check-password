import pytest
from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("S@1word") is False  # менше 8 символів


def test_too_long_password() -> None:
    assert check_password("Pass@word1234567890") is False  # більше 16 символів


def test_missing_uppercase() -> None:
    assert check_password("pass@word1") is False  # немає великої літери


def test_missing_digit() -> None:
    assert check_password("Password@") is False  # немає цифри


def test_missing_special_char() -> None:
    assert check_password("Password1") is False  # немає спецсимволу


def test_invalid_characters() -> None:
    assert check_password("Pass@word1_+") is False  # + не дозволений


@pytest.mark.parametrize("password", [
    "GoodPass1@",  # валідний
    "Another#1!",  # валідний
    "BadPass?",    # ? не дозволений
    "noDigit@",    # немає цифри
    "12345678",    # тільки цифри, немає літер і спецсимволу
])
def test_various_passwords(password: str) -> None:
    expected = password in ["GoodPass1@", "Another#1!"]
    assert check_password(password) is expected
