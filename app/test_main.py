import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Amweeyt11", False),
        ("Qhj3rty_9&@3", True),
        ("A56jdnwhjkl90876$!-", False),
        ("kdQ_0", False),
        ("HkhlKhgf*_", False),
        ("wkkdks876$_", False),
    ],
    ids=[
        "Special character missing",
        "Valid password",
        "Password length more then 16 symbols",
        "Password length less then 8 symbols",
        "Digits missing",
        "Uppercase letters missing"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
