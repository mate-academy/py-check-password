import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expect",
    [
        ("1L3#2", False),
        ("123456789123456f@OL", False),
        ("password1@", False),
        ("passwordA@", False),
        ("Qwert1jy", False),
    ]
)
def test_check_password(password: str, expect: bool) -> None:
    assert check_password(password) == expect
