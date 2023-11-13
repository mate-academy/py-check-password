import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("qwerty1!", False),
        ("Qwerty11", False),
        ("Qwerty!@", False),
        ("Qwert1@", False),
        ("Qwerty12345!@#!@3", False)
    ]
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected
