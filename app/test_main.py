import pytest

from app import main


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Aa1$567", False),
        ("Aa1$5678901234567", False),
        ("a1$56789", False),
        ("Aa$aaaaa", False),
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Aa156789", False),
        ("Aa1$5678", True),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert main.check_password(password) == expected
