# app/test_main.py
from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password_exact_boundary() -> None:
    # Exactly 7 characters -> invalid
    assert check_password("Abc1@xy") is False


def test_too_long_password_exact_boundary() -> None:
    # Exactly 17 characters -> invalid
    assert check_password("Abcdefghijk1@LMNO") is False


def test_missing_special_character() -> None:
    assert check_password("Password1") is False


def test_missing_digit() -> None:
    assert check_password("Password@") is False


def test_missing_uppercase_letter() -> None:
    assert check_password("pass@word1") is False


def test_invalid_characters() -> None:
    # Contains invalid symbol '%'
    assert check_password("Pass%word1") is False


def test_min_length_valid_password() -> None:
    # Exactly 8 chars -> valid
    assert check_password("Abcdef1@") is True


def test_max_length_valid_password() -> None:
    # Exactly 16 chars -> valid
    assert check_password("Abcdefghij1@KLM") is True
