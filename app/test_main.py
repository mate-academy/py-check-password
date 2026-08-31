import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("Str@ngPass1@", True),
    ("StrngPass1", False),
    ("str@ngpass1", False),
    ("Str@ngPass", False),
    ("Short1!", False),
    ("ThisPasswordIsWayTooLong1!", False),
    ("Valid1@password", True),
    ("Va1id$@pass", True),
    ("Va1id@-pass", True),
    ("Va1id@pass#", True),
    ("Invalid_char*", False),
    ("NoDigit!", False),
    ("NoSpecialCharacter1", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
