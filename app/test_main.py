import pytest
from app.main import check_password


@pytest.mark.parametrize("password, boll",
                         [
                             ("", False),
                             ("@", False),
                             ("1", False),
                             ("A", False),
                             ("Art1d@!", False),
                             ("Aft12@!", False),
                             ("Paswort@", False),
                             ("paswort@", False),
                             ("paswor1@", False),
                             ("pasworte", False),
                             ("12345678", False),
                             ("!@#$%^&*", False),
                             ("Passwo@1", True),
                             ("Passwo@1#", True),
                             ("Passwort@2DSds2", True),
                             ("Passwort@2DSds23", True),
                             ("Passwortf2DSds23", False),
                             ("Passwort@2ffdffsfscdsfsdf", False),
                             ("passwort@2DSds23^", False)
                         ])
def test_check_password(password: str, boll: bool) -> None:
    assert check_password(password) == boll
