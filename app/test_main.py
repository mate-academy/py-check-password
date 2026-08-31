import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("aA12@", False),
        ("$@#&!-_", False),
        ("$@#&!-jdjkrjr", False),
        ("$@#1A&!-_", True),
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Str@HH1HHHGGGGGGG", False),
        ("Aa$GFHFHFFH", False),
        ("a1GGDGGDGH", False),
        ("pass@word1", False),
    ]

)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
