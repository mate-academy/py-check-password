import pytest
from app.main import check_password


def test_should_return_true_for_valid_password() -> None:
    password = "Pass@word1"

    assert check_password(password) is True


def test_should_return_false_for_short_password() -> None:
    password = "Abef1@"

    assert check_password(password) is False


def test_should_return_true_for_8_len_password() -> None:
    password = "Abcdef1@"

    assert check_password(password) is True


def test_should_return_true_for_16_len_password() -> None:
    password = "Abcdefghijklm1@x"

    assert check_password(password) is True


def test_should_return_false_for_17_len_password() -> None:
    password = "Abcdefghijklmn1@x"

    assert check_password(password) is False


def test_should_check_uppercase_symbols() -> None:
    password = "password1@"

    assert check_password(password) is False


def test_should_check_digits_symbols() -> None:
    password = "Password@"

    assert check_password(password) is False


def test_should_check_special_symbols() -> None:
    password = "Password1"

    assert check_password(password) is False


def test_should_check_forbidden_symbols() -> None:
    password = "Pass*word1"

    assert check_password(password) is False


def test_should_return_false_for_non_latin_letter() -> None:
    password = "PassworД1@"

    assert check_password(password) is False


def test_should_return_false_for_space() -> None:
    password = "Pass word1@"

    assert check_password(password) is False


@pytest.mark.parametrize("special", ["$", "@", "#", "&", "!", "-", "_"])
def test_should_accept_allowed_special_characters(special: str) -> None:
    password = f"Password1{special}"

    assert check_password(password) is True
