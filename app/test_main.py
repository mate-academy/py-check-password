import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("qwertyqwertyqwerty", False),
        ("password1@", False),
        ("Password1", False),
        ("Pass word1@", False),
        ("Password1*", False),
        ("Пароль1@", False),
        ("Aa1@", False),
        ("VeryLongPassword1@#", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
