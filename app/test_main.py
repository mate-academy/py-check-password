from app.main import check_password


def test_too_short() -> None:
    assert check_password("Qwer1&") is False


def test_amount_of_upper() -> None:
    assert check_password("Password1") is False


def test_special_character_in_password() -> None:
    assert check_password("Str@ng") is False


def test_password_without_upper_latters() -> None:
    assert check_password("mountains1&") is False


def test_too_long() -> None:
    assert check_password("qwertyAsfvfvbfdbdf12&") is False


def test_password_without_digits() -> None:
    assert check_password("Mountains&") is False
