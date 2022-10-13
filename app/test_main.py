import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_data",
    [
        pytest.param(
            "Password@1", True,
            id="the password was made with upper, "
               "digit, special and in range 8-16"
        ),
        pytest.param(
            "password@1", False,
            id="the password was made with no uppercase letter"
        ),
        pytest.param(
            "Password@", False,
            id="the password was made with no digit"
        ),
        pytest.param(
            "Password1", False,
            id="the password was made with no special character"
        ),
        pytest.param(
            "Pass@1", False,
            id="the password was made with less than 8 characters"
        ),
        pytest.param(
            "Pass@wordPass@word1", False
        ),
    ]
)
def test_check_password(
        password: str,
        expected_data: bool
) -> None:
    assert check_password(password) == expected_data
