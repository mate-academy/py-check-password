from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word", False),
        ("password1@", False),
        ("PASS1@WORD", True),
        ("Pass word1@", False),
        ("Pass@1", False),
        ("Pass@word1word1word", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
