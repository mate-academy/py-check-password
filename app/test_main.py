import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("1A@", False),
        ("A1@bcdefghijklmnop", False),
        ("Password1", False),
        ("Password@", False),
        ("password1@", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
