import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_bool",
    [
        (pytest.param("Password1$", True, id="Correct")),
        (pytest.param("password1$", False, id="without uppercase")),
        (pytest.param("Pawod1$", False, id="len less then 8")),
        (pytest.param("Passwor1$dhgydqyn", False, id=" too long passwords")),
        (pytest.param("Password$h", False, id="without digits")),
        (pytest.param("Password1h", False, id="without spec-symbols")),
        (pytest.param("passhй$h", False, id="should be only latin alphabet"))
    ]
)
def test_check_password(
        password: str,
        expected_bool: bool) -> None:
    assert check_password(password) == expected_bool
