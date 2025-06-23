from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "pass_try, result",
    [
        ("Password1!", True),
        ("password1!", False),
        ("Password!", False),
        ("Password1", False),
        ("Passw1!", False),
        ("PasswordPassword1!", False),
    ]
)
def test_check_password(pass_try: str, result: bool) -> None:
    assert check_password(pass_try) == result
