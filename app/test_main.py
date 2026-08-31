import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_value",
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
def test_check_password(password: str, expected_value: bool) -> None:
    assert check_password(password) == expected_value
