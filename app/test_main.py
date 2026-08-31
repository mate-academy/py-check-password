import pytest
from app.main import check_password


def test_valid_passwords() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("A1b@Cdef") is True
    assert check_password("1A!b2C#d3E4") is True


def test_invalid_passwords() -> None:
    assert check_password("") is False
    assert check_password("qwerty") is False
    assert check_password("Str@ng") is False
    assert check_password("LongPassword1234567890!") is False
    assert check_password("short1@") is False
    assert check_password("NoDigitsOrSpecialChar") is False
    assert check_password("12345678") is False
    assert check_password("!@#$%^&") is False
    assert check_password("A1b@") is False
    assert check_password("A@longpassword") is False


def test_edge_cases() -> None:
    assert check_password("A1@aaaaaaa") is True
    assert check_password("A1@aaaaaaaaaaaaaaa") is False
    assert check_password("A1@aaaaaaaaaaaaaaaa") is False
    assert check_password("A1@") is False
    assert check_password("A1") is False


@pytest.mark.parametrize(
    "password, expected",
    [
        ("", False),
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("A1b@Cdef", True),
        ("A1@verylongpassword", False),
        ("12345678$@", False),
        ("1A!b2C#d3E4", True),
        ("LongPassword1234567890!", False),
        ("short1@", False),
        ("NoDigitsOrSpecialChar", False),
        ("12345678", False),
        ("!@#$%^&", False),
        ("A1b@", False),
        ("A1@aaaaaaa", True),
        ("A1@aaaaaaaaaaaaaaa", False),
        ("A1@aaaaaaaaaaaaaaaa", False),
        ("A1@", False),
        ("A1", False),
    ]
)
def test_password_parametrized(password: str, expected: bool) -> None:
    assert check_password(password) == expected
