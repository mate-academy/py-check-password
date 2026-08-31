import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Valid1@Password", True),
        ("12345678", False),
        ("Special1@Char#", True),
        ("Short1@", False),
        ("TooLongPassword1@", False),
        ("NoDigitPassword@", False),
        ("NoSpecialChar1", False),
        ("nouppercase1$", False)
    ],
    ids=[
        "valid_password",
        "too_short",
        "too_short_and_without_digit",
        "valid_password",
        "only_digits",
        "valid_password_with_special_char",
        "too_short_with_special_char",
        "too_long_with_special_char",
        "no_digit",
        "no_special",
        "no_uppercase",
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    """
    Test the check_password function to ensure it returns the correct
    boolean value based on the validity of the password.

    Parameters:
    - password (str): The password string to check.
    - expected (bool): The expected result of the password check.
    """
    assert check_password(password) == expected, (
        f"Expected {expected} for password {password}, "
        f"but got {check_password(password)}"
    )
