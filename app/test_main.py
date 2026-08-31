import pytest

from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("strin2gng@g", False),
    ("Super@Password213567", False),
    ("Super@Password", False),
    ("P@s123", False),
    ("Super2Password", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
