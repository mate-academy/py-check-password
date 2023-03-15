import pytest
from app.main import check_password


@pytest.mark.parametrize("password, result", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("Str@ng", False),
    ("", False),
    ("Pass@word", False),
    ("Pass@word12345678", False),
    ("pass@word1", False),
    ("P1assaword", False),
    ("P1@word", False)
])
def test_check_password(password: str,
                        result: bool) -> None:
    assert check_password(password) == result
