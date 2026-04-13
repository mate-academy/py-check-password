import pytest


from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Ab1$5678", True),
    ("A1$bcdefghij890k", True),
    ("Short1!", False),
    ("WayTooLong123456@A", False),
    ("", False),
    ("NoSpecial1", False),
    ("NoDigits@", False),
    ("nouppercase1@", False),
    ("ONLYUPPER123!", True),
    ("Pass word1!", False),
    ("Pass@word1%", False),
    ("Pássword1!", False),
], ids=[
    "valid_standard",
    "min_length_8",
    "max_length_16",
    "too_short",
    "too_long",
    "empty_string",
    "missing_special",
    "missing_digit",
    "missing_uppercase",
    "missing_lowercase",
    "illegal_space",
    "illegal_symbol",
    "non_latin_chars"
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
