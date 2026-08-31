from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Abc@1234") is True


def test_invalid_length_short() -> None:
    assert check_password("Abc@12") is False


def test_invalid_length_long() -> None:
    assert check_password("Abc@12345678901234567890") is False


def test_invalid_no_digit() -> None:
    assert check_password("Abc@defgh") is False


def test_invalid_no_special_char() -> None:
    assert check_password("Abcdefgh123") is False


def test_invalid_no_uppercase() -> None:
    assert check_password("abc@1234") is False


def test_valid_minimum_length() -> None:
    assert check_password("Aa@1") is False


def test_valid_maximum_length() -> None:
    assert check_password("Aa@1" + "a" * 9) is True
