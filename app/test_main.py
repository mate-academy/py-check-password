from app import main


def test_valid_password() -> None:
    assert main.check_password("Pass@word1") is True


def test_password_too_short() -> None:
    assert main.check_password("Pas@wd1") is False


def test_password_too_long() -> None:
    assert main.check_password("Password@123456789") is False


def test_password_missing_uppercase() -> None:
    assert main.check_password("password@1") is False


def test_password_missing_digit() -> None:
    assert main.check_password("Password@") is False


def test_password_missing_special_char() -> None:
    assert main.check_password("Password123") is False


def test_password_invalid_characters() -> None:
    assert main.check_password("Pass@word1%") is False


def test_password_boundary_min_length() -> None:
    assert main.check_password("P@ssw0rd") is True


def test_password_boundary_max_length() -> None:
    assert main.check_password("P@ssw0rd12345678") is True
