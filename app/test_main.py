import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("12345678", False),
    ("Password!", False),
    ("@1A", False),
    ("LongPassword123$", True),
    ("Valid$Pass1", True),
    ("Short7$", False),
    ("ValidPassword123$", False),
    ("NoSpecialChar1", False),
    ("nouppercase1$", False),
    ("NOLOWERCASE1$", True),
    ("Special@@1A", True),
    ("1234567890123456", False),
    ("@@@@@@@@@@1A", True),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
