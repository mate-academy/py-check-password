import pytest
from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Abcdef1@") is True


def test_too_short_password() -> None:
    assert check_password("Ab1@") is False


def test_too_long_password() -> None:
    assert check_password("Abcdefghijklmn1@X") is False


def test_missing_uppercase() -> None:
    assert check_password("abcdefg1@") is False


def test_missing_digit() -> None:
    assert check_password("Abcdefgh@") is False


def test_missing_special_character() -> None:
    assert check_password("Abcdefg1") is False


def test_invalid_special_character() -> None:
    assert check_password("Abcdefg1*") is False


def test_non_ascii_letter() -> None:
    assert check_password("Ábcdef1@") is False


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("ABCDEFG@", False),
        ("12345678@", False),
        ("Abcdefgh1", False),
        ("Abc1@", False),
        ("A" * 20 + "1@", False)
    ]
)
def test_multiple_cases(password: str, expected: bool) -> None:
    assert check_password(password) is expected
