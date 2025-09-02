from app.main import check_password


def test_check_password_has_at_least_eight_symbols() -> None:
    password = "Pas@wo1"
    assert check_password(password) is False


def test_check_password_has_maximum_sixteen_symbols() -> None:
    password = "MyPass@@word_123!"
    assert check_password(password) is False


def test_check_password_has_number() -> None:
    password = "Pass@_word"
    assert check_password(password) is False


def test_check_password_has_special_symbol() -> None:
    password = "PASSWORD1"
    assert check_password(password) is False


def test_check_password_has_one_upper_case() -> None:
    password = "pass@_word121"
    assert check_password(password) is False
