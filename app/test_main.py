from .main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_short_password() -> None:
    assert check_password("Abc@123") is False


def test_long_password() -> None:
    assert check_password("Abc@123456789012345") is False


def test_no_uppercase() -> None:
    assert check_password("abc@1234") is False


def test_no_digit() -> None:
    assert check_password("Abc@defgh") is False


def test_no_special_character() -> None:
    assert check_password("Abcdefgh1234") is False


def test_invalid_character() -> None:
    assert check_password("Abc@1234*") is False


def test_non_latin_alphabet() -> None:
    assert check_password("Секрет@123") is False
