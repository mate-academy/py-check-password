import pytest
from app.main import check_password

# Valid passwords


@pytest.mark.parametrize("password", [
    "Pass@word1",
    "AaBbC123$",
    "AbCdEfGh$9-",
    "AbcDefg$1",
    "A@B1cdEfgh_"
])
def test_valid_passwords(password: any) -> None:
    assert check_password(password) is True

# Invalid passwords


@pytest.mark.parametrize("password", [
    "qwerty",          # Less than 8 characters
    "Str@ng",          # No digit
    "Password12",      # No special character
    "abcdEFGH12345",  # More than 16 characters
    "invalidpass",     # No special character
    "P@$$word",        # Less than 8 characters
])
def test_invalid_passwords(password: any) -> None:
    assert check_password(password) is False
