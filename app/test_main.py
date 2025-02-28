import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("PASSWORD1@", True),
    ("pass@word1", False),
    ("PASSWORD@", False),
    ("Password1", False),
    ("Pass@1", False),
    ("Pass@1234567890123", False),
    ("12345678@", False),
    ("Password@", False),
    ("Pa$$w0rd", True),
    ("!@#&-_123A", True),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
