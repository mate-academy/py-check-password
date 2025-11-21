import pytest
from typing import Any

from app.main import check_password


@pytest.mark.parametrize(
    "string, result", [
        ("Str@ng1", False),
        ("Str@ng12", True),
    ]
)
def test_string_length_min(string: str, result: bool) -> Any:
    assert check_password(string) == result


@pytest.mark.parametrize(
    "string, result", [
        ("Pass@word1Pass@__", False),
        ("Pass@word1Pass@_", True),
    ]
)
def test_string_length_max(string: str, result: bool) -> Any:
    assert check_password(string) is result


def test_string_have_upper_letter() -> Any:
    assert check_password("pass@word1") is False


def test_string_have_digit() -> Any:
    assert check_password("Pass@words") is False


def test_string_have__special_symbols() -> Any:
    assert check_password("passwords1") is False


@pytest.mark.parametrize(
    "string, result", [
        ("strongs", False),
        ("Pass@wordPass", False),
        ("pass@words", False),
        ("Password123", False),
        ("strongs23445", False),
    ]
)
def test_have_needed_characters(string: str, result: bool) -> Any:
    assert check_password(string) is result
