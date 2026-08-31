import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        ("Pass@word1", True),
        ("pass$word1", False),
        ("Password1", False),
        ("Pass@word", False),
        (" password ", False),
        ("Str@ng1", False),
        ("Password13Dian@!!", False),
        ("Password13Dian@!", True),

    ],
    ids=[
        "should_contain_digit_&_special_character_&_uppercase",
        "should_also_contain_uppercase_letter",
        "should_also_contain_special_character",
        "should_also_contain_digit",
        "should_not_contain_spaces",
        "should_be_at_least_8_characters",
        "should_not_contain_more_than_16_characters",
        "should_maximum_contain_16_characters",
    ]
)
def test_if_checking_is_correct(
        password: str,
        is_valid: bool
) -> None:
    assert check_password(password) == is_valid
