# write your code here
from app.main import check_password


def test_password_for_required_symbols() -> None:
    assert check_password("Password1") is False  # no special character
    assert check_password("Password@") is False  # no digit
    assert check_password("passw0rd@") is False  # no uppercase letter


def test_password_for_min_length() -> None:
    assert check_password("Pas1@rd") is False


def test_password_for_max_length() -> None:
    assert check_password("Passwooooooooord1@") is False
