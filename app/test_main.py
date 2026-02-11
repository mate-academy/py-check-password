import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Password@1", True),  # valid: proper length, upper, digit, special
        ("Password@1Password@1", False),  # too long: 18 chars (max 16)
        ("password@1", False),  # no uppercase letter
        ("Password@", False),  # no digit
        ("Password1", False),  # no special character
        ("Pass1", False),  # too short, only 5 chars
        ("Pass@1", False),  # too short: 6 chars
    ],
)
def test_check_password(password: str, expected: str) -> None:
    assert check_password(password) is expected
