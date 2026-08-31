import pytest


from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("coolpassword", False),
    ("Coolpassword", False),
    ("Password1", False),
    ("Str@ng1", False),
    ("passw@rd1", False),
    ("Pass@word", False),
    ("Pass@word1233456789", False),
    ("Pass@word123", True),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
