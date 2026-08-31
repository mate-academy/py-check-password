from app.main import check_password


def test_for_non_latin_alphabet_in_password() -> None:
    assert check_password("GFds#1fghап") is False


def test_for_non_digit_in_password() -> None:
    assert check_password("GFds#fghgf") is False


def test_for_non_special_numbers_in_password() -> None:
    assert check_password("GFd1sfghgf") is False


def test_if_password_have_less_then_8_digits() -> None:
    assert check_password("GFd1#") is False


def test_if_password_have_more_then_16_digits() -> None:
    assert check_password("GFdsdafdhdhrtgdfhgshg1#") is False
