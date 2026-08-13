import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@word1",
    "A1@aaaaa",
    "Strong1#",
    "Valid123$",
    "Abcdef1!",
    "Z9&yyyyy",
    "Qwerty1-",
    "Test1234_",
    "A1@bcdefghijklmn"
])
def test_valid_passwords(password: str) -> None:
    assert check_password(password) is True


def test_too_short() -> None:
    assert check_password("A1@aaaa") is False


def test_too_long() -> None:
    assert check_password("A1@abcdefghijklmnop") is False


def test_missing_digit() -> None:
    assert check_password("Password@") is False


def test_missing_special_char() -> None:
    assert check_password("Password1") is False


def test_missing_uppercase() -> None:
    assert check_password("password1@") is False


@pytest.mark.parametrize("password", [
    "Password1*",
    "Password1%",
    "Пароль1@",
    "Password1 @"
])
def test_invalid_characters(password: str) -> None:
    assert check_password(password) is False


def test_exact_min_length() -> None:
    assert check_password("A1@aaaaa") is True


def test_exact_max_length() -> None:
    assert check_password("A1@abcdefghijklm") is True


def test_empty_string() -> None:
    assert check_password("") is False


def test_only_required_minimum_types_but_short() -> None:
    assert check_password("A1@a") is False


def test_only_letters_and_digits() -> None:
    assert check_password("Password123") is False
