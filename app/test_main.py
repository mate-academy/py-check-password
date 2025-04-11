import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result_bool",
    [
        pytest.param(
            "Pass@3",
            False,
            id="Too short password test"
        ),
        pytest.param(
            "Passwo@#e",
            False,
            id="No digit test"
        ),
        pytest.param(
            "Passwo1234",
            False,
            id="No special character test"
        ),
        pytest.param(
            "Passworrrd123456789@#!",
            False,
            id="Too long password test"
        ),
        pytest.param(
            "password12!@",
            False,
            id="No upper letter test"
        )
    ]
)
def test_check_password(
        password: str,
        result_bool: bool
) -> None:
    assert check_password(password) == result_bool
