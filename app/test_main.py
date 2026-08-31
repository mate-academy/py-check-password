# write your code here
from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short() -> None:
    # Test for passwords that are too short
    assert check_password("Short1@") is False


def test_missing_uppercase() -> None:
    # Test for passwords without uppercase letters
    assert check_password("no_upper1@") is False


def test_missing_digit() -> None:
    # Test for passwords without digits
    assert check_password("NoDigit@") is False


def test_missing_special_character() -> None:
    # Test for passwords without special characters
    assert check_password("NoSpecial1") is False


def test_too_long() -> None:
    # Test for passwords that are too long
    assert check_password("VeryLongPassword@1234") is False


def test_invalid_character() -> None:
    # Test for passwords with invalid characters (e.g., non-Latin symbols)
    assert check_password("Invalid1@€") is False


def test_all_lowercase() -> None:
    # Test for passwords with only lowercase letters
    assert check_password("lowercase1@") is False


def test_only_digits_and_special() -> None:
    # Test for passwords with only digits and special characters
    assert check_password("12345678@") is False


def test_edge_case_exact_8_chars() -> None:
    # Test for passwords that are exactly 8 characters long and valid
    assert check_password("P@ssw0rd") is True


def test_edge_case_exact_16_chars() -> None:
    # Test for passwords that are exactly 16 characters long and valid
    assert check_password("P@ssword1234567") is True
