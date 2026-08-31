import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param(
            "Password1!",
            True,
            id="The password is valid."
        ),
        pytest.param(
            "Pass1!",
            False,
            id="The password length should be at least 8 characters."
        ),
        pytest.param(
            "Password$Password4",
            False,
            id="The password length should be less than 16 characters."
        ),
        pytest.param(
            "Password!",
            False,
            id="The password should contain at least 1 digit."
        ),
        pytest.param(
            "Password1",
            False,
            id="The password should contain at least 1 special character."
        ),
        pytest.param(
            "password1!",
            False,
            id="The password should contain at least 1 uppercase letter."
        ),
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
