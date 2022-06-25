import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Paaaaaaaaaaass@word1", False),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass@word", False),
        ("P@d1", False),
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result
