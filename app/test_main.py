import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        # VALID CASES
        pytest.param(
            "Qwerty@1",
            True,
            id="valid_min_length",
        ),
        pytest.param(
            "Qwertyu@1",
            True,
            id="valid_regular",
        ),
        pytest.param(
            "Qwertyuiopasdf@1",
            True,
            id="valid_max_length",
        ),

        # LENGTH RULES
        pytest.param(
            "Qwert@1",
            False,
            id="too_short",
        ),
        pytest.param(
            "Qwertyuiopasdf@12",
            False,
            id="too_long",
        ),

        # MISSING REQUIRED PARTS
        pytest.param(
            "qwerty@1",
            False,
            id="no_uppercase",
        ),
        pytest.param(
            "Qwertyu1",
            False,
            id="no_special_char",
        ),
        pytest.param(
            "Qwerty@a",
            False,
            id="no_digit",
        ),
        pytest.param(
            "Qwertyag",
            False,
            id="only_letters",
        ),
        pytest.param(
            "12345678",
            False,
            id="only_digits",
        ),
        pytest.param(
            "$@#&!-_@",
            False,
            id="only_special_chars",
        ),

        # INVALID CHARACTERS
        pytest.param(
            "Qwerty@1Ж",
            False,
            id="non_latin_cyrillic",
        ),
        pytest.param(
            "Qwerty@1ß",
            False,
            id="non_ascii_letter",
        ),
        pytest.param(
            "Qwerty@1*",
            False,
            id="invalid_symbol",
        ),
        pytest.param(
            "Qwerty@1 ",
            False,
            id="contains_space",
        ),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
