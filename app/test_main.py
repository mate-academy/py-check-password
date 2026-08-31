import pytest

import app.main as main


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("1234567A!", True),
        ("Short1!", False),
        ("ThisIsAVeryLongPassword123!", False),
        ("qwerty", False),
        ("Password123", False),
        ("Password!", False),
        ("Password123$", True),
        ("Password123@", True),
        ("Password123#", True),
        ("Password123&", True),
        ("Password123!", True),
        ("Password123-", True),
        ("Password123_", True),
        ("Password123%", False),
        ("Password123*", False),
        ("Password123()", False),
        ("Password123<", False),
    ],
)
class TestCheckPassword:
    def test_check_password(self, password: str, expected: bool) -> None:
        assert main.check_password(password) == expected

    def test_check_upper_letter(self, password: str, expected: bool) -> None:
        assert main.check_password("password123!") is False
