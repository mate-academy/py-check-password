import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("Ps@wd1", False),
        ("Ps@wd109cc0909097", False),
        ("Pass@word1", True)
    ],
    ids=[
        "Password without any digits should return False",
        "Password without any special character should return False",
        "Password without any uppercase letter should return False",
        "Password shorter than 8 characters should return False",
        "Password longer than 16 characters should return False",
        "Pass@word1 should return True"
    ],
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
