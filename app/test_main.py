import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("12345678", False),
    ("Password1", False),
    ("Pass@word", False),
    ("P@1", False),
    ("Valid@Pass123", True),
    ("TooL0ng@Password123", False),
    ("NoSpecChar1", False),
    ("@A1abcdef", True),
    ("A1@1234567890123", True),
    ("lowercase@1", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
