from app.main import check_password


def test_should_return_false_if_no_uppercase_letters() -> None:
    assert check_password("pycharm!2022") is False


def test_should_return_false_if_no_digit() -> None:
    assert check_password("Pycharm!") is False


def test_should_return_false_if_no_special_character() -> None:
    assert check_password("Pycharm2022") is False


def test_should_return_false_for_short_passwords() -> None:
    assert check_password("Py!20") is False


def test_should_return_false_when_password_bigger_16() -> None:
    assert check_password("pytestPycharm!2022") is False


def test_should_return_false_when_symbol_incorrect() -> None:
    assert check_password("%пайчармPytest") is False


def test_should_return_true_for_valid_password() -> None:
    assert check_password("Pytest!2022") is True
