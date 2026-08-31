import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word1Pass@word1", False),
        ("P@ss1", False),
        ("Pass@:word1", False),
        ("Пароль123@", False),
        ("1234567898", False),
        ("$@#&!-_$@#&!-_", False),
        ("Pass @word1", False),
        ("pAss@word1", True),
        ("1Pass@word1", True),
        ("Pass@word", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected, (
        "Password isn`t correct"
    )
