import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Q2rt@", False),
    ("Str@ng", False),
    ("12345678", False),
    ("Password", False),
    ("password", False),
    ("Password1", False),
    ("password1@", False),
    ("Password1@", True),
    ("ThisIsAValidPassword123!", False),
    ("TooLongPassword123!", False),
    ("ShortP@ss", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
