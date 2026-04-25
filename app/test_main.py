import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("A@bcd1234", True),
        ("abcd1234", False),
        ("A@b1", False),
        ("jhlkh@klrlfk3k333ffdRRFf4", False),
        ("Abcd1234", False),
        ("abcdgg4h", False),
        ("A@bcdefg", False),
        ("abc@3ggdh", False),
    ],
    ids=[
        "valid_password",
        "missing_uppercase",
        "too_short",
        "too_long",
        "missing_special_char",
        "missing_uppercase_and_special_char",
        "missing_digit",
        "only_small_chars"
    ]
)
def test_password_checker(password: str, result: bool) -> None:
    assert check_password(password) == result
