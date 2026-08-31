from app.main import check_password


def test_should_return_false_when_password_less_than_8_symbols() -> None:
    assert check_password("Qwer1@") is False


def test_should_return_false_when_password_more_than_16_symbols() -> None:
    assert check_password("Qwertyuiopasdfghjklzxcvb1@") is False


def test_should_return_false_when_all_symbols_are_lower() -> None:
    assert check_password("qwertyu1@") is False


def test_should_return_false_when_there_is_no_digit_in_password() -> None:
    assert check_password("Qwertyui@") is False


def test_should_return_false_when_password_without_special_symbols() -> None:
    assert check_password("qwerty1234") is False


def test_should_return_true_when_password_is_valid() -> None:
    assert check_password("Qwerty1@34") is True
