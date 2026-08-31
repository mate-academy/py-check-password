import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Password123", False),
        ("Password@!", False),
        ("password@1", False),
        ("PASSWORD@1", True),
        ("P@1", False),
        ("ThisIsAVeryLongPassword1@", False),
        ("Valid1@password", True),
        ("InvalidPassword#", False),
        ("No$pecialChar123", True),
        ("Valid@1pass", True),
        ("Invalid!password", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
