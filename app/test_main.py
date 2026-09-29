import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "Abcdef1$",
        "Abcdefghijk1$xyz",
        "A123456@",
        "Abcdefg1$",
        "Abcdefg1_",
        "Abcdefg1-",
        "Abcdefg1!",
        "Abcdefg1&",
        "Abcdefg1#",
    ],
)
def test_valid_passwords(password):
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "",
        "A1@bcde",  # 7 characters
        "Abcdefghijk1@$xyz",  # 17 characters
        "qwerty1@",  # no uppercase letter
        "Abcdefg@",  # no digit
        "Abcdefg1",  # no special character
        "Abcdef1?",  # unsupported punctuation
        "Abcdef1 ",  # whitespace
        "Äbcdef1@",  # non-Latin letter
        "Abcdef١@",  # non-ASCII digit
    ],
)
def test_invalid_passwords(password):
    assert check_password(password) is False


def test_password_length_boundaries_are_inclusive():
    assert check_password("A1@bcde") is False
    assert check_password("Abcdefg1$") is True
    assert check_password("Abcdefghijk1$xyz") is True
    assert check_password("Abcdefghijk1@$xyz") is False
