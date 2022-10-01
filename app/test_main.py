from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Fa1$",
            False,
            id="should has at least 8 characters"
        ),
        pytest.param(
            "Passwordistoolongforthisfunction123@",
            False,
            id="should has maximum 16 characters inclusive"
        ),
        pytest.param(
            "justpassword123@",
            False,
            id="should has at least one uppercase letter A-Z"
        ),
        pytest.param(
            "Password123",
            False,
            id="should contains at least one special characters"
        ),
        pytest.param(
            "Password@$!",
            False,
            id="should contains at least one digit"
        ),
        pytest.param(
            "Password123@$!",
            True,
            id="should return 'True' if password is valid"
        )
    ]
)
def test_check_password_correctly(password, result) -> None:
    assert check_password(password) == result
