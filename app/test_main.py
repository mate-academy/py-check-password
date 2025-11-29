import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Strong#Pass9", True),
        ("A1@bcdefg", True),
        ("Str@ng", False),
        ("A1@bc", False),
        ("VeryLongPassword@123", False),
        ("password1@", False),
        ("Password@", False),
        ("Password1", False),
        ("Pass word1@", False),
        ("qwertyui", False),
    ],
    ids=[
        "valid_example",
        "valid_strong",
        "valid_min_length",
        "too_short",
        "too_short2",
        "too_long",
        "missing_uppercase",
        "missing_digit",
        "missing_special",
        "invalid_char_space",
        "only_lowercase",
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
