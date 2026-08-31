import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Qw@y1", False, id="test for too short"),
        pytest.param("Qwert@1", False, id="test for shorter for 1 symbol"),

        pytest.param("Qwert@qwertqwertqwert1", False, id="test for too long"),
        pytest.param(
            "Qwerty1!Qwerty1@a", False, id="test longer for 1 symbol"
        ),

        pytest.param("Qwerty123", False, id="test for no special"),
        pytest.param(
            "qwerty123", False, id="test for no uppercase and special"
        ),
        pytest.param("qwerty!123", False, id="test for no uppercase"),
        pytest.param("Qwertyqwerty@", False, id="test for no digit"),
        pytest.param("123456!@#&", False, id="test for no letters"),
        pytest.param("qwertyqwert", False, id="test for just lowercase"),
        pytest.param("Qwerty123@%", False, id="test for forbidden symbols"),

        pytest.param("Qwerty1!", True, id="test for min possible len"),
        pytest.param("Qwerty1!Qwerty1@", True, id="test for max possible len"),
        pytest.param("Qwerty123!#", True, id="test valid"),
        pytest.param(
            "Alpha1!$@#&!-_", True, id="test valid with all possible symbols"
        ),

    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
