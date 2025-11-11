from app.main import check_password


def test_valid_password_typical() -> None:
    assert check_password("Pass@word1") is True


def test_should_check_min_length() -> None:
    assert check_password("A1@bcde") is False


def test_should_check_max_length() -> None:
    assert check_password("A1@abcdefghijklmnop") is False


def test_should_check_digit() -> None:
    assert check_password("Abc@defg") is False


def test_should_check_special_symbols() -> None:
    assert check_password("Abcdefg1") is False


def test_should_check_upper_letter() -> None:
    assert check_password("abc@def1") is False
