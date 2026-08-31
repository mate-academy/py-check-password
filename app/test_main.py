import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Pass?word1", False),
        ("Qw3#ty", False),
        ("T0olongof@password", False),
        ("Passsword1", False),
        ("Pass@word", False),
        ("pass@word1", False),
    ],
    ids=[
        "check a valid password",
        "password is not valid, if invalid characters are used",
        "password is not valid, if doesn't reach 8 characters",
        "password is not valid, when more than 16 characters",
        "password is not valid, if no special characters",
        "password is not valid, if no digits",
        "password is not valid, if no uppercase letters",
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
