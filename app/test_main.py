import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("pass@word1", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("", False),
        ("Abcdefghijklmnopqrstuvwxyz1@!", False),  # Too long
        ("1234567890", False),
        ("LongEnough1$", True),
        ("Nospecialchar123", False),  # Missing special character
        ("NoDigits@", False),  # Missing digit
        ("ABCDEFGHIJKLMNOP", False),  # Only uppercase letters
        ("12345678", False),  # Only digits
        ("!@#$%^&*()_+", False),  # Only special characters
        ("MixOfCharacters", False),  # Missing digit
        ("aBcD1234!@#$", True),  # Valid password
        ("1a!B", False),  # Too short
        ("Aa1!Aa1!Aa1!Aa1!", True),  # Just Ok
    ]
)
def test_passwords(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
