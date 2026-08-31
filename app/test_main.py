import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("<PASSWORD>", False),
        ("Qwerty!@#", False),
        ("$Tr0ng", False),
        ("Password123!@#4561", False),
        ("password123!@#", False),
        ("Password123", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
