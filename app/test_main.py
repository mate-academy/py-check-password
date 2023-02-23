import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,access",
    [
        pytest.param(
            "Password@1",
            True,
            id="test correct password length"
        ),
        pytest.param(
            "Pass@1",
            False,
            id="test password length less then 8"
        ),
        pytest.param(
            "PasswordPasswordPassword@1",
            False,
            id="test password length greater then 16"
        ),
        pytest.param(
            "12345678@",
            False,
            id="test password without any letter"
        ),
        pytest.param(
            "password1@",
            False,
            id="test password without any upper letter"
        ),
        pytest.param(
            "Password@",
            False,
            id="test password without any digit"
        ),
        pytest.param(
            "Password1",
            False,
            id="test password without any special symbol"
        )
    ]
)
def test_check_password(password: str, access: bool) -> None:
    assert check_password(password) is access
