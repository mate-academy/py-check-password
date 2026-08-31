import pytest

from app.main import check_password


@pytest.mark.parametrize("password, result", [
    ("Passwo@rd1", True),
    ("qwerty", False),
    ("", False),
    ("Str@ng", False),
    ("P@word1", False),
    ("Paлsроo@d1", False),
    ("P@word1klklgfdgglk12hUGGHJ", False)
])
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
