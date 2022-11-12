from app.main import check_password


def test_password_length() -> None:
    assert check_password("Passw1!") is False


def test_password_digits() -> None:
    assert check_password("Password!") is False


def test_password_too_long() -> None:
    assert check_password("Password1!Password1!") is False


def test_password_have_uppercase_letter() -> None:
    assert check_password("password1!") is False
