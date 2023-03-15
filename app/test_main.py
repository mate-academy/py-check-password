from app.main import check_password


def test_no_digits_in_password() -> None:
    password = "Password@"

    assert check_password(password) is False


def test_no_upper_character_in_password() -> None:
    password = "password1@"

    assert check_password(password) is False


def test_no_special_character_in_password() -> None:
    password = "Password1"

    assert check_password(password) is False


def test_too_short_password() -> None:
    password = "Pasd1@"

    assert check_password(password) is False


def test_too_long_password() -> None:
    password = "Password1@Password1@Password1@"

    assert check_password(password) is False


def test_correct_password() -> None:
    password = "Password1@"

    assert check_password(password)
