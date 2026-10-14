from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("Pass@word1qwerty") is True


def test_should_check_min_length() -> None:
    assert check_password("Pass@w1") is False


def test_should_check_upper_later() -> None:
    assert check_password("pass@word1") is False


def test_should_check_digit() -> None:
    assert check_password("Pass@word") is False


def test_should_check_special_symbols() -> None:
    assert check_password("password1") is False


def test_max_length() -> None:
    assert check_password("Pass@word1qwertypo") is False
