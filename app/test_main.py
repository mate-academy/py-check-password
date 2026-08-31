from app.main import check_password


def test_should_check_min_length() -> None:
    assert check_password("Aa1$aaa") is False


def test_should_check_max_length() -> None:
    assert check_password("Aa1$aaaaaaaaaaaaaa") is False


def test_should_check_upper_letter() -> None:
    assert check_password("aa1$aaaa") is False


def test_should_check_digit() -> None:
    assert check_password("Aa$aaaaa") is False


def test_should_check_special_symbols() -> None:
    assert check_password("Aa1aaaaa") is False


def test_valid_password() -> None:
    assert check_password("Aa1$aaaa") is True
