from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@1", False),
        ("ThisIsVeryLongPassword123!", False),
        ("Password@Abc", False),
        ("Password123", False),
        ("password@123", False),
        ("Pass@word1", True),
        ("Valid@Pass#1", True),
        ("ValidPass@123456", True),
        ("Invalid@пароль1", False),
    ]
)
def test_check_password(password: str, expected: bool,) -> None:
    assert check_password(password) == expected
