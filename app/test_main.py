import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "Abcdef1$",
        "Abcdef1@",
        "Abcdef1#",
        "Abcdef1&",
        "Abcdef1!",
        "Abcdef1-",
        "Abcdef1_",
        "A123456$",
        "Abcdefghijk1$",
        "A" + "a" * 13 + "1$",
    ],
)
def test_accepts_valid_passwords(password: str) -> None:
    assert check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "A12345$",  # 7 characters
        "A" + "a" * 14 + "1$",  # 17 characters
        "qwerty",  # too short and missing required character types
        "Abcdefg$",  # no digit
        "abcdefg1$",  # no uppercase letter
        "Abcdefg1",  # no special character
        "Abcdef 1$",  # whitespace is not allowed
        "Abcdef1%",  # unsupported punctuation
        "Äbcdef1$",  # non-Latin letter
        "Abcdef١$",  # non-ASCII digit
        "Abcdef１$",  # full-width digit
    ],
)
def test_rejects_invalid_passwords(password: str) -> None:
    assert check_password(password) is False
