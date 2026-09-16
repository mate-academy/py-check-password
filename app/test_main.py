import pytest
from app import main


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("fhj!", False),
        ("fghjk", False),
        ("A@12345", False),
        ("Password1", False),
        ("password1@", False),
        ("PASSWORD1@", True),
        ("Pass123*", False),
        ("Pass@1234567890", True),
        ("Pass@12345678910!", False),
        ("Pass@word", False),
        ("Pass@word!", False),
        ("Pass@word1!", True),
        ("Pass@word1$", True),
        ("Pass@word1%", False),
        ("Pass word1@", False)
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert main.check_password(password) == expected
