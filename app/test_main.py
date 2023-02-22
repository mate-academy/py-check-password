import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Asd1_", False,
            id="password is short"
        ), pytest.param(
            "Ajsld_123_!!jdsmcjsfha", False,
            id="length is too long"
        ), pytest.param(
            "password1_", False,
            id="password is not capitalized"
        ), pytest.param(
            "Password_", False,
            id="the password does not have a number"
        ), pytest.param(
            "Password1", False,
            id="password has no special character"
        ), pytest.param(
            "Password1!", True,
            id="password access"
        )
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
