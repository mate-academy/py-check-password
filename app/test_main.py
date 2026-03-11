import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "12445F!", False,
            id="should return 'False' if password length "
               "is less than 8 characters"
        ),
        pytest.param(
            "12345fF!", True,
            id="should return 'True' if password length "
               "is more than 7 characters"
        ),
        pytest.param(
            "1234567891234fF!", True,
            id="should return 'True' if password length "
               "is between 8 and 16 characters"
        ),
        pytest.param(
            "1234567891234fF!1", False,
            id="should return 'False' if password length "
               "is more than 16 characters"
        ),
        pytest.param(
            "qwFffqwqw!", False,
            id="should return 'False' if 'digit' not in password"
        ),
        pytest.param(
            "2134ad!12", False,
            id="should return 'False' if "
               "'uppercase letter' not in password"
        ),
        pytest.param(
            "2134Ad2e21", False,
            id="should return 'False' if "
               "'special character' not in password"
        )
    ]
)
def test_modify_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
