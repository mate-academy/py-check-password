import pytest
from app.main import check_password


@pytest.fixture
def options_password() -> list[dict]:
    return [
        {
            "min_length": "8"
        },
        {
            "max_length": "16"
        },
        {
            "latin_letters": "Aa-Zz"
        },
        {
            "digits": "0-9"
        },
        {
            "special_character": "$@#&!-_"
        }
    ]


def test_should_check_min_length(options_password: list[dict]) -> None:
    password = "Abcde@1"
    result = check_password(password)
    assert result is False


def test_should_check_max_length(options_password: list[dict]) -> None:
    password = "Abcdef@1234567890"
    result = check_password(password)
    assert result is False


def test_should_check_upper_letter(options_password: list[dict]) -> None:
    password = "abcdef@1"
    result = check_password(password)
    assert result is False


def test_should_check_digit(options_password: list[dict]) -> None:
    password = "Abcdef@a"
    result = check_password(password)
    assert result is False


def test_should_check_special_symbols(options_password: list[dict]) -> None:
    password = "Abcdef12"
    result = check_password(password)
    assert result is False
