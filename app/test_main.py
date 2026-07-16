import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid_password",
    [
        ("Pass@word1", True),
        ("paSs$@#&!-_123", True),
        ("Pas#war7", True),
        ("passwordPass@3#4", True),
        ("passwordPass@3#4drowssap", False),
        ("password#1", False),
        ("Password1", False),
        ("Pass$1", False),
        ("Pass@word", False)
    ]
)
def test_check_password(password: str, is_valid_password: bool) -> None:
    assert check_password(password) == is_valid_password
