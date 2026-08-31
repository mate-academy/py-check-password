import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("P@ss1234", True),
        ("P@ssword12345678", True),
        ("P@ss123", False),
        ("P@ssword123456789", False),
        ("Password123", False),
        ("Pass@word", False),
        ("pass@word1", False),
        ("Pass@word1%", False),
        ("Пароль@123", False),
        ("qwerty", False),
        ("jk1@", False),
    ]
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected
