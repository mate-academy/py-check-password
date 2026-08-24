import pytest

from app.main import check_password


@pytest.mark.parametrize("password,expected_result", [
    ("Pass@word1", True),
    ("1Wr!y", False),
    ("Str@ng!!!", False),
    ("f8Str@ng!f8Str@ng", False),
    ("f8trng!f8trng", False),
    ("f8trngf8trnPg", False),
], ids=["Valid",
        "Too short",
        "No digit",
        "Too long",
        "No Uppercase",
        "No special symbol"])
def test_check_password(password: str, expected_result: bool) -> None:

    assert check_password(password) == expected_result
