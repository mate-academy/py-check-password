import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result", [
        ("password", False),
        ("Password1", False),
        ("Password1$", True),
        ("Password1$Password1$", False),
        ("password1$", False),
        ("Password$", False),
        ("1Password$", True),
        ("Pass1$", False)
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
