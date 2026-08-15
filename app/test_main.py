import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("a" * 7, False),
        ("a" * 17, False),
        ("Пароль1!", False),
        ("a" * 8, False),
        ("a" * 8 + "A", False),
        ("a" * 8 + "A!", False),
        ("a" * 8 + "A!9", True),
    ],
    ids=[
        "Password length less than 7",
        "Password length greater than 16",
        "Password contains cyrillic letters",
        "Password contains only letters",
        "Password contains only lower and upper letters",
        "Password contains only lower, upper letters and symbols",
        "Password contains only lower/upper letters, symbols and numbers",
    ]
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected
