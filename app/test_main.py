from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_password_too_short() -> None:
    assert check_password("Ab1@abc") is False


def test_password_too_long() -> None:
    assert check_password("Password12345678@") is False


def test_password_without_uppercase() -> None:
    assert check_password("password1@") is False


def test_password_without_digit() -> None:
    assert check_password("Password@") is False


def test_password_without_special_character() -> None:
    assert check_password("Password1") is False


def test_password_with_invalid_character() -> None:
    assert check_password("Password1?") is False


def test_password_minimum_length() -> None:
    assert check_password("Abcdef1@") is True


def test_password_maximum_length() -> None:
    assert check_password("Password12345@A") is True
