from app.main import check_password


def test_password_length_at_least_8_letters() -> None:
    assert check_password("Taras@2") is False
    assert check_password("Taras!22")


def test_password_length_less_16_characters() -> None:
    assert check_password("Taras12345678__21") is False


def test_letters_in_password() -> None:
    assert check_password("1234567@") is False
    assert check_password("T123456@")


def test_special_symbols_in_password() -> None:
    assert check_password("$@#&!-_a0T")
    assert check_password("Taras099_%") is False


def test_digits_in_password() -> None:
    assert check_password("Taras__@") is False


def test_password_contains_digit_spec_char_upp_letter() -> None:
    assert check_password("tarasssss") is False
    assert check_password("Taras_1233")
