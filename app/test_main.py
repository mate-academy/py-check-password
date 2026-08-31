import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Pass@word1", True),
        ("Correct@word1!", True),
        ("A1@bcdefghijklmn", True),
        ("A1@bcdefghijklmnop", False),
        ("qwerty", False),
        ("Password@", False),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass.word1@", False),
        ("Pass word1@", False),
        ("Str@ng", False),
        ("", False),
        ("Пар@!оль123", False),
    ],
    ids=[
        "valid_basic",
        "valid_with_extra_special",
        "valid_max_length",
        "too_long_17_chars",
        "no_digit_no_special_no_upper",
        "no_digit",
        "no_uppercase",
        "no_special_char",
        "invalid_char_dot",
        "invalid_char_space",
        "too_short",
        "empty_string",
        "non_latin_characters",
    ]
)
def test_check_password(input_data: str, expected: bool) -> None:
    assert check_password(input_data) == expected
