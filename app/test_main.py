import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("12345678", False),
        ("Pass@word", False),
        ("Pass", False),
        ("HelloWorld@1234567890HAHAHA", False),
        ("asd@1234567", False),
        ("A@1", False),
        ("Qwerty123", False),

    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
