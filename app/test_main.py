import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Qwerty1$@#&!-_", True, id="Correct password"),
        pytest.param("Qwe&5", False, id="Length less then 8"),
        pytest.param("@Qwerty$8Qwerty8!", False, id="Length more then 16"),
        pytest.param("@Qwerty 8!", False, id="Wrong simbol in password"),
        pytest.param("qwerty$8-8!", False, id="No uppercase in password"),
        pytest.param("$@#&!-_$@#&!", False, id="No letter in password"),
        pytest.param("Qwerty$Qwerty", False, id="No digit in password"),
        pytest.param("QwertyJohn1", False, id="No special symbol"),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
