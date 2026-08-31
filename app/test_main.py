import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("Qwerty123@", True),
        ("Qwert1@", False),
        ("Qwerty1234567890@", False),
        ("Qwerty@@@", False),
        ("Qwerty123", False),
        ("qwerty123@", False),
    ],
    ids=[
        "test correct password",
        "test less than 8 characters",
        "test more than 16 characters",
        "test no digits",
        "test no special characters",
        "test no uppercase letters",
    ]
)
def test_passwords(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
