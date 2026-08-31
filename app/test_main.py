import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "A1@bcdef",
        "Strong-Password1",
        "Z9_abcdef",
    ],
)
def test_check_password_returns_true_for_valid_passwords(
    password: str,
) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "A1@bcde",
        "",
    ],
)
def test_check_password_returns_false_for_too_short_passwords(
    password: str,
) -> None:
    assert check_password(password) is False


def test_check_password_returns_false_for_too_long_password() -> None:
    assert check_password("StrongPassword12@") is False


@pytest.mark.parametrize(
    "password",
    [
        "password1@",
        "pass_word1",
    ],
)
def test_check_password_returns_false_without_uppercase_letter(
    password: str,
) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize(
    "password",
    [
        "Password@",
        "Qwerty-u",
    ],
)
def test_check_password_returns_false_without_digit(password: str) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize(
    "password",
    [
        "Password1",
        "StrongPass2",
    ],
)
def test_check_password_returns_false_without_special_character(
    password: str,
) -> None:
    assert check_password(password) is False


@pytest.mark.parametrize(
    "password",
    [
        "Pass word1@",
        "Passwорд1@",
        "Password1%",
    ],
)
def test_check_password_returns_false_for_invalid_characters(
    password: str,
) -> None:
    assert check_password(password) is False
