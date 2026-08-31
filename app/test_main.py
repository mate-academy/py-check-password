import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Qwert1!", False, id="False if password is lower 8 char"
        ),
        pytest.param(
            "Qwertyyyyyyyyyy1!", False, id="False if password longer 16 char"
        ),
        pytest.param(
            "Qwertyy!", False, id="False if password has no numbers"
        ),
        pytest.param(
            "Qwertyy1", False, id="False if password has no special char"
        ),
        pytest.param(
            "qwerty1!", False, id="False if password has no uppercase letters"
        ),
        pytest.param(
            "Qwerty1!", True, id="True if all conditions is True"
        ),
    ]
)
def test_func_should_confirm_password_if_all_conditions_is_true(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
