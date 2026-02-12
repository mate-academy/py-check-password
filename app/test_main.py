import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Abcdefgh1$Xyz", True),
        ("VeryLongPassword1$", False),
        ("Password1", False),
        ("password1@", False),
        ("Pässword1@", False),
        ("Пароль1@", False),
        ("Password1*", False),
        ("Pass word1@", False),
        ("1234567$", False),
        ("Password123", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result
