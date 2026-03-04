import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    pytest.param("Pass@word1", True,
                 id="Given password valid, good length and strong"),
    pytest.param("qwerty", False,
                 id="Given password is an invalid, length < 8"),
    pytest.param("Aaaaaaa1", False,
                 id="Weak passwords are not allowed, no special character"),
    pytest.param("Aaaaaaa@", False,
                 id="Weak passwords are not allowed, no digits"),
    pytest.param("aaaaa1@", False,
                 id="Weak passwords are not allowed, no uppercase"),
    pytest.param("", False,
                 id="Empty password not allowed"),
    pytest.param("Nhjgjcathf25@asqe", False,
                 id="password lengh more than 16"),
    pytest.param("Nhjgj cathf25@", False,
                 id="Password can't include whitespaces"),])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
