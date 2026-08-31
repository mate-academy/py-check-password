import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("qwerty22@dwq", False),
    ("Str@ng", False),
    ("Password1", False),
    ("12345678", False),
    ("$trongPass1", True),
    ("P@ssw0rd", True),
    ("Pass_word1", True),
    ("TooLongPassword1@#", False),
    ("Short1!", False),
    ("NoDigitSpecial", False),
    ("$peci@lCh@r@cter", False),
    ("Strong$Password_1", False)
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
