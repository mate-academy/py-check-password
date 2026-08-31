from app.main import check_password


def test_should_check_min_length() -> None:
    """
    the minimal length is 8
    """

    pw_true = "Pass@wo1"
    pw_false = "Pas@w1"

    assert check_password(pw_true) == (len(pw_true) >= 8)
    assert check_password(pw_false) == (len(pw_false) >= 8)


def test_should_check_max_length() -> None:
    """
    the maximal length is 16 inclusive
    """

    pw_true = "LangesPasswort@1"
    pw_false = "ZuLangesPasswort@123"

    assert check_password(pw_true) == (len(pw_true) <= 16)
    assert check_password(pw_false) == (len(pw_false) <= 16)


def check_special_char(password: str) -> bool:
    special_characters = "$@#&!-_"

    return any(char in special_characters for char in password)


def check_digit_in_string(password: str) -> bool:
    digits = "0123456789"

    return any(char in digits for char in password)


def check_upper_letter(password: str) -> bool:
    return any(char.isupper() for char in password)


def test_should_check_accepted_characters() -> None:
    """
    - accepts only letters of the Latin alphabet Aa-Zz, digits 0-9
    or special character from `$@#&!-_`;
    - contains at least 1 digit, 1 special character, 1 uppercase letter.
    """

    assert check_password("Pass@word1") == check_special_char("Pass@word1")
    assert check_password("Password1") == check_special_char("Password1")

    assert check_password("Pass@word1") == check_digit_in_string("Pass@word1")
    assert check_password("Pass@word") == check_digit_in_string("Pass@word")
    assert check_password("Str@ng") == check_digit_in_string("Str@ng")

    assert check_password("Pass@word1") == check_upper_letter("Pass@word1")
    assert check_password("pass@word1") == check_upper_letter("pass@word1")
    assert check_password("qwerty") == check_upper_letter("qwerty")
