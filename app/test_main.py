from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True,
                     id="valid password"),
        pytest.param("pass@word1", False,
                     id="no uppercase letter"),
        pytest.param("Pass@word", False,
                     id="no digit"),
        pytest.param("Password1", False,
                     id="no special symbol"),
        pytest.param("1234", False,
                     id="too short"),
        pytest.param("TooLongPassword!1", False,
                     id="too long"),
        pytest.param("Pass@w0rd", True,
                     id="valid password with different symbols and digits"),
        pytest.param("Pass@w0rD", True,
                     id="valid password with different uppercase letters"),
        pytest.param("Pass@1", False,
                     id="valid symbols and digits but too short"),
        pytest.param("Pass@word123", True,
                     id="valid symbols and digits but too long"),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
