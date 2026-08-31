from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="Should be 'True' when password is 'Pass@word1'"
        ),
        pytest.param(
            "Ps@1",
            False,
            id="Password must be between longer than 8 characters"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="Password should have at least one uppercase letter"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="Password should have at least one digit"
        ),
        pytest.param(
            "Pass@word12flet$gfv",
            False,
            id="Password must be shorter than 16 characters"
        ),
        pytest.param(
            "Passsword1",
            False,
            id="Password must have at least one special character"
        )
    ]
)
def test_password_work_correctly(
        password: str,
        result: str
) -> None:
    assert check_password(password) == result
