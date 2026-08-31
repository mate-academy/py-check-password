import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result", [
        ("Qw@1ty", False),
        ("Qwertyuiopry1", False),
        ("Qwertyui$", False),
        ("Qwert@івап1", False),
        ("qwe1@rty", False),
        ("Qw1@rtyujhgfdcvbn", False),
        ("Qwerty1@", True)
    ],
    ids=[
        "Must be at least 8 characters",
        "Must contain at least one special character",
        "Must contain at least one digit",
        "Must contain only Latin letters",
        "Must contain at least one upper case",
        "Too long. Maximum 16 characters",
        "Password is accepted!"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
