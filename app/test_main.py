import pytest

from app.main import check_password


@pytest.mark.parametrize("password,expected", [
    ("        ", False),
    ("pass", False),
    ("P@6s", False),
    ("password", False),
    ("Password", False),
    ("p@ssword", False),
    ("passw0rd", False),
    ("P@ssword", False),
    ("p@ssw0rd", False),
    ("Passw0rd", False),
    ("P@ssw0rd", True),
    ("P@ssw0rd ", False),
    ("P@ssw0rdP@ssw0rdP@ssw0rd", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
