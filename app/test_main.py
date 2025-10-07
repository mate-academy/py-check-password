from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Psw1!", False),
        ("Nodigits!", False),
        ("password1!", False),
        ("Sr@ng1Sr@ng1Sr@ng1Sr@ng1Sr@ng1", False),
        ("Password12345", False),
        ("Password1!", True)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
