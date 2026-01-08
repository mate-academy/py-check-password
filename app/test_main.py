import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Secur#ty1", True),
    ("123Aa@!_", True),
    ("A1@bcdef", True),
    ("A1@bcdefghijklmn", True),
    ("Test$123", True),
    ("Test@123", True),
    ("Test#123", True),
    ("Test&123", True),
    ("Test!123", True),
    ("Test-123", True),
    ("Test_123", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("A1@bcd", False),
    ("A1@bcde", False),
    ("A1@bcdefghijklmno", False),
    ("", False),
    ("pass@word1", False),
    ("Pass@word", False),
    ("Password12", False),
    ("Pass word1", False),
    ("Pass^word1", False),
    ("Pass%word1", False),
    ("Pass(word1", False),
    ("Pass/word1", False),
    ("Pass.word1", False),
    ("Pass1!ф", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
