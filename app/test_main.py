from app.main import check_password


def test_valid_password() -> None:
    # Test a valid password that meets all the criteria
    assert check_password("Pass@word1"), "Valid password should return True"


def test_short_password() -> None:
    # Test a password shorter than 8 characters
    assert not check_password("P@ss1"), "Password shorter than 8 "


def test_long_password() -> None:
    # Test a password longer than 16 characters
    assert not check_password("VeryLongPass@word1"), "Password longer than 16"


def test_password_without_digit() -> None:
    # Test a password without any digits
    assert not check_password("Password@"), "Password without"


def test_password_without_special_character() -> None:
    # Test a password without any special characters
    assert not check_password("Password1"), "Password without"


def test_password_without_uppercase() -> None:
    # Test a password without any uppercase letters
    assert not check_password("pass@word1"), "Password without"


def test_password_with_invalid_characters() -> None:
    assert not check_password("Pass@word1*"), "Password with invalid"


def test_password_just_right_length() -> None:
    # Test a password that is exactly 8 characters long
    assert check_password("Pass@8d1"), "Password is 8"


def test_password_maximum_length() -> None:
    # Test a password that is exactly 16 characters long
    assert check_password("Pass@word1234Aa"), "Password that is exactly 16"
