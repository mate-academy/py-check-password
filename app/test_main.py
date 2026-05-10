import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("1234567A#", True),
        ("A1#asdfghjklpoki", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("VeryLongPassword123#@", False),
        ("OnlyLetters!", False),
        ("onlydigits123!", False),
        ("NoSpecial123A", False),
        ("Albeda.Star1", False),
        ("CyrillicИ1#", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
