import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, bool_result",
    [
        pytest.param(
            "Pass@word1", True,
            id="password is correct"
        ),
        pytest.param(
            "Тsіwo@@rd", False,
            id="password should not consist cyrillic letters"
        ),
        pytest.param(
            "Pass@word1Pass@word1Pass@word1", False,
            id="password shouldn't contain more than 16 characters"
        ),
        pytest.param(
            "012345678", False,
            id="password shouldn't contain only digit"
        ),
        pytest.param(
            "", False,
            id="password shouldn't be empty"
        ),
        pytest.param(
            "Pass@word", False,
            id="password should contain at least 1 digit"
        ),
        pytest.param(
            "Password11", False,
            id="password should contain at least 1 special character"
        ),
        pytest.param(
            "pass@@word11", False,
            id="password should contain at least 1 uppercase letter"
        ),
        pytest.param(
            "Pa@wor1", False,
            id="password should contain at least 8 characters"
        ),
    ]
)
def test_check_password(password: str, bool_result: bool) -> None:
    assert check_password(password) == bool_result
