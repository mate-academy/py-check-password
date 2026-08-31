import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Str@ng", False),
    ("Password!", False),
    ("Password1", False),
    ("pass@word1", False),
    ("Pass@word1*", False),
    ("Pass@word1Pass@word1", False),
    ("Pas@w1rd", True),
    ("Password@12345", True),
    ("Pa1@", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
