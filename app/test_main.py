from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("", False),
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
        ("ShortP@ss", False)
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
