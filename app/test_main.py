import pytest
from app.main import check_password


@pytest.mark.parametrize("password,expected", [
    ("Pas@1", False),
    ("Pass@word1", True),
    ("pasword", False),
    ("PASSWORD1", False),
    ("pa111ord", False),
    ("PASSW11", False),
    ("Password", False),
    ("Pass@word12345", True),
    ("Pass@word123456", True),
    ("Pass@word12345678", False),
    ("Пароль123@", False),
    ("Pass@word!1", True),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
