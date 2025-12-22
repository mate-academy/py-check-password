import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("paass@word1", False),
    ("qwerty", False),
    ("Str@ng", False),
    ("Pass@word1_Pass@word1_Pass@word1_Pass@word1", False),
    ("Pass@1", False),
    ("Pass@word", False),
    ("Password123", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
