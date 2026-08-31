from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "is_valid, password",
    [
        (True, "Pass@word1"),
        (False, "tomatoes"),
        (False, "Str@nggg"),
        (False, "qwerty19"),
        (False, "Qwe7rty3"),
        (False, "Tomatoes"),
        (False, "Pas_o1"),
        (False, "Pass@word1sdfdfsf__-sdfsdf"),
        (False, "pass@word1")
    ],
    ids=[
        "correct password",
        "Please add 1+ uppercase letter, 1+ digit, 1+ special character",
        "Please add 1+ digit",
        "Please add 1+ special character, 1+ uppercase letter",
        "Please add 1+ special character",
        "Please add 1+ special character, 1+ digit",
        "Please use 8-16 characters",
        "Password too long. Please use 8-16 characters",
        "Please add 1+ uppercase letter"
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid, \
        "Password should be: accepts only letters" \
        " of the Latin alphabet Aa-Zz," \
        " digits 0-9 or special character from $@#&!-_. " \
        "At least 8 characters. " \
        "Maximum 16 characters inclusive. " \
        "Contains at least 1 digit, 1 special character, 1 uppercase letter."
