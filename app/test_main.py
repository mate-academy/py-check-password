import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Long_long_long_long_long_password$@#&!-_12345", False),
        ("Pass$@#&!", False),
        ("P@ss1", False),
        ("Password123", False),
        ("password!1", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) is result
