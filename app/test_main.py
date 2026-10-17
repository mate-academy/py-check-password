import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("A1b$cdef", True),
        ("P@ssword12345678", True),
        ("Test#999", True),
        ("Pas@1", False),
        ("P@ssword123456789", False),
        ("Pass@word1 ", False),
        ("Пароль@123", False),
        ("Pass%word1", False),
        ("password@1", False),
        ("Password!", False),
        ("Password1", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
