# flake8: noqa: *
import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("Pass@word1", True, id="Correct password"),
        pytest.param("qwert1@", False, id="Short password"),
        pytest.param("qeeqweqweqweq1qwert@", False, id="Long password"),
        pytest.param("Pass@wordd", False, id="No digit"),
        pytest.param("Passsword1", False, id="No symbol"),
        pytest.param("pass@word1", False, id="No uppercase letter"),
        pytest.param("Pass@word1%", False, id="Invalid character %"),
        pytest.param("Pass word1@", False, id="Space in password"),
        pytest.param("Пароль1@", False, id="Non-latin letters")
    ]
)
def test_check_password_logic(password, expected):
    assert check_password(password) == expected