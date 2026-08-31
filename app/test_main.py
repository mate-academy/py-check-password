import pytest

from .main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass1!", False),
        ("Password1!", True),
        ("Password!", False),
        ("Password1", False),
        ("password1!", False),
        ("PasswordPassword!!1", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
