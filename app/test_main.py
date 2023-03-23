from app.main import check_password


def test_should_return_false_when_password_has_7_symbols() -> None:
    assert check_password("As&4567") is False


def test_should_return_false_when_password_has_17_symbols() -> None:
    assert check_password("As&45678901234567") is False


def test_should_return_false_when_password_has_not_upper_letters() -> None:
    assert check_password("s&45678901234") is False


def test_should_return_false_when_password_has_no_symbols() -> None:
    assert check_password("As45678901234") is False


def test_should_return_false_when_password_has_no_digits() -> None:
    assert check_password("A&d&a&a&d") is False
