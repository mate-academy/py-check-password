from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("1Qwert@", False,
                     id="password should contain at least 8 characters"),
        pytest.param("Pass@word1Pass@word1", False,
                     id="password should contain maximum 16 characters"),
        pytest.param("Pass@word1Pass@word1", False,
                     id="password should contain maximum 16 characters"),
        pytest.param("Pass@word", False,
                     id="password should contain at least 1 digit"),
        pytest.param("Password1", False,
                     id="password should have at least 1 special character"),
        pytest.param("pass@word1", False,
                     id="password should contain at least 1 uppercase letter"),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
