from app.main import check_password


def test_check_password_without_special_symbols() -> None:
    assert check_password("Password1") is False


def test_check_password_short_passwords() -> None:
    assert check_password("Pa$1") is False


def test_check_password_too_long_passwords() -> None:
    assert check_password("PasswordPa$$wordandmanymanywords1") is False


def test_check_password_without_uppercase_letter() -> None:
    assert check_password("pa$sword1") is False


def test_check_password_without_digits() -> None:
    assert check_password("Pa$sword") is False


def test_check_password_no_password() -> None:
    assert check_password("") is False


def test_check_password_true_password() -> None:
    assert check_password("Pas$worD1") is True
