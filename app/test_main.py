import app.main as main


def test_valid_password() -> None:
    assert main.check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert main.check_password("Aa1@abc") is False


def test_minimum_length() -> None:
    assert main.check_password("Aa1@abcd") is True


def test_maximum_length() -> None:
    assert main.check_password("Aa1@aaaaaaaaaaaa") is True


def test_too_long_password() -> None:
    assert main.check_password("Aa1@aaaaaaaaaaaaa") is False


def test_without_uppercase() -> None:
    assert main.check_password("password1@") is False


def test_without_digit() -> None:
    assert main.check_password("Password@") is False


def test_without_special_character() -> None:
    assert main.check_password("Password1") is False


def test_invalid_character() -> None:
    assert main.check_password("Password1%") is False
