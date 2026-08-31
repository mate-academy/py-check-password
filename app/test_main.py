from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("1Q!qwe", False),
        ("Str@ngdfgjh", False),
        ("!W1qwertyuiasdfghjkl", False),
        ("1qweQtixcv", False),
        ("1!zxcvbnmjht", False),
        ("Q!zxcvbnmjht", False)
    ]
)
def test_password_return_bool(password: str, result: bool) -> None:
    assert check_password(password) == result
