from .main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Pass@word1", True,
                     id="function runs correctly"),
        pytest.param("qqqweRty1", False,
                     id="passwort should have at least 1 special character"),
        pytest.param("qweQWE!@#", False,
                     id="password should have at least 1 digit"),
        pytest.param("qwerty12!@", False,
                     id="password should have at least 1 uppercase letter"),
        pytest.param("Str@ng1", False,
                     id="password is too short"),
        pytest.param("aaaaAAAA1234!@#$0", False,
                     id="password is too long"),
        pytest.param("qWerty123?", False,
                     id="forbidden character")
    ]
)
def test_function_runs_correctly(
        password: str,
        result: bool) -> None:
    assert check_password(password) == result
