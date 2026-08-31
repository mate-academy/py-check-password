import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        ("Val1dP@ss", True),
        ("Sh0rt_", False),
        ("TooLooooooongPassw0rd#", False),
        ("qwerty5_", False),
        ("N0thingSpecia1", False),
        ("TwoPlusTwo-_-", False),
        ("N0TCreative?", False),
        ("M8 Academy!", False),
    ],
    ids=[
        "Valid password",
        "Invalid password: shorter than 8 characters",
        "Invalid password: longer than 16 characters",
        "Invalid password: no uppercase",
        "Invalid password: no special characters",
        "Invalid password: no digits",
        "Invalid password: not allowed characters",
        "Invalid password: spaces"
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
