import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("", False),
        ("Pass@word123456789", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("PassWord1", False),
        ("Pass@word1!", True),
        ("P@ss1", False),
        ("Pass@word123456", True),
        ("Password123456", False),
        ("Pass", False),
        ("Pass@word123456234", False),
        ("Passsdfretf", False),
        ("Passworert", False),
        ("Passworddddd", False),
        ("password123456", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
