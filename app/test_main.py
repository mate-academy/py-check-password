import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    pytest.param("Pass@word1", True,
                 id="Given password valid, good length and strong"),
    pytest.param("Q5@", False,
                 id="returns False for short password"),
    pytest.param("Nhjgdgsthf25", False,
                 id="Weak passwords are not allowed, no special character"),
    pytest.param("Nhqqqcathf@", False,
                 id="Weak passwords are not allowed, no digits"),
    pytest.param("Nheerrathf25@asqe", False,
                 id="password lengh more than 16"),
    pytest.param("Nhjgj cathf25@", False,
                 id="Password can't include whitespaces"),
    pytest.param("nhrrttcathf25@", False,
                 id="Weak passwords are not allowed, "
                    "no upper case letter in password"),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
