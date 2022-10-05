from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Password@1",
            True,
            id="return true if has upper, digit, special and in range 8-16"
        ),
        pytest.param(
            "password@1",
            False,
            id="return false if no uppercase letter"
        ),
        pytest.param(
            "Password@",
            False,
            id="return false if no digit"
        ),
        pytest.param(
            "Password1",
            False,
            id="return false if no special character"
        ),
        pytest.param(
            "Pass@1",
            False,
            id="return false if less than 8 characters"
        ),
        pytest.param(
            "Pass@wordPass@word1",
            False,
            id="return false if more than 16 characters"
        ),

    ]
)
def test_return_false_if_less_than_8_characters(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
