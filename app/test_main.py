import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),  # Валідний пароль
    ("qwerty", False),  # Немає цифр або спецсимволів
    ("Str@ng", False),  # Менше 8 символів
    ("NoNumber@", False),  # Немає цифр
    ("Short1!", False),  # Менше 8 символів
    ("THIS@ISVALID1", True),  # Валідний пароль
    ("onlylowercase1!", False),  # Немає великої літери
    ("NoSpecialSymbol1", False),  # Немає спецсимволу
    ("$$$$$$$", False),  # Немає літер та цифр
    ("Valid_Password1!", True),  # _ не дозволений
    ("TooLongPassword1!!!", False),  # Більше 16 символів
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
