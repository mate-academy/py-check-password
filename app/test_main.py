import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),  # Valid password
        ("Str@ngPassword123456", False),  # Too long
        ("password@123", False),  # No uppercase letter
        ("Password@", False),  # No digit
        ("Password123", False),  # No special character
        ("Pass&word1", True),  # Invalid character
        ("P@ss1w", False),
    ],
    ids=[
        "valid_password",
        "too_long_password",
        "no_uppercase_letter",
        "no_digit",
        "no_special_character",
        "invalid_character",
        "short_password",
    ],
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
