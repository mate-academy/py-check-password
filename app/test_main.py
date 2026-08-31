from app.main import check_password


def test_check_password() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("qwerty") is False
    assert check_password("Str@ng") is False


def test_should_check_min_length() -> None:
    assert check_password("qweQ2@") is False


def test_should_check_special_symbols() -> None:
    assert check_password("wer123QWE") is False


def test_should_check_digit() -> None:
    assert check_password("qweEW#$#") is False


def test_should_check_upper_letter() -> None:
    assert check_password("e@wqerw123") is False


def test_should_check_max_length() -> None:
    assert check_password("123456789!@#$qQWER") is False
