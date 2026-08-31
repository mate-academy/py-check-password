import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("ABC123@", False),
        ("ABCDE12345$@#&!-_", False),
        ("ABCD$@#&!-_", False),
        ("ABCDE12345", False),
        ("12345$@#&!", False),
        ("ABCDE12345$@#&!", True)
    ],
    ids=[
        "Length of password must be at least 8 characters",
        "Length of password must be at not grater than 16 characters",
        "Password must contain at least 1 digit",
        "Password must contain at least 1 special character",
        "Password must contain at least 1 uppercase letter",
        "Valid password should return True"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
