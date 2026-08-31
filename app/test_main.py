import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Password@1", True),
        ("Passw@1", False),
        ("PasswordPassword@1", False),
        ("Password@", False),
        ("Password1", False),
        ("password@1", False)
    ],
    ids=[
        "Password meets all the rules",
        "Password must have at least 8 characters",
        "Password must have maximum 16 characters inclusive",
        "Password contains at least 1 digit",
        "Password contains at least 1 special character",
        "Password contains at least 1 uppercase letter"
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
