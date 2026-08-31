from app.main import check_password


def test_correct_password() -> None:
    assert check_password("Pass@word1") is True


def test_incorrect_password_no_numbers() -> None:
    assert check_password("Pass@word") is False


def test_incorrect_password_no_special_symbols() -> None:
    assert check_password("Password121") is False


def test_incorrect_password_no_letters() -> None:
    assert check_password("$@#&!-_121") is False


def test_incorrect_password_lowercase() -> None:
    assert check_password("password-123") is False


def test_correct_password_uppercase() -> None:
    assert check_password("PASSWORD-123") is True


def test_incorrect_too_short_password() -> None:
    assert check_password("Pass-1") is False


def test_incorrect_too_long_password() -> None:
    assert check_password("My@Super-puprer&pass-word!!!1") is False
