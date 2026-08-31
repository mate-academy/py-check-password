import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Password@", False),  # missing digit
        ("Password1", False),  # missing special character
        ("password1@", False),  # missing uppercase
        ("TooLongPassword123!@#", False),  # too long
        ("J@h1", False),  # should be invalid, as it's too short
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
