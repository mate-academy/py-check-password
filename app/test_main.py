from unittest import mock

import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        ("qwerty", False),
        ("Pass@word1", True),
        ("Str@ng", False),
        ("NoDigitsOrSpecialChar", False),
        ("NoSpecialChars1", False),
        ("TooLongPassword123$!", False),
        ("Invalid@Char1&*", False),
        ("1Short!", False),
        ("nouppercase1$", False),
        ("wiThoutdig$", False)
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    with mock.patch("app.main.ascii_lowercase", "abcdefghijklmnopqrstuvwxyz"):
        assert check_password(password) == is_valid
