from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("Qwerty", False),
        ("qwerty", False),
        ("@@@", False),
        ("Str@1ng", False),
        ("AAAAAAAAAAAAaA@1A", False),
        ("", False),
        ("Lambda@#$", False),
        ("Lambda123", False),
        ("lambda12@", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
