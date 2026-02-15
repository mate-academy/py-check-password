from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("qwerty") is False


def test_no_special_character_password() -> None:
    assert check_password("Strng123") is False


def test_no_digit_password() -> None:
    assert check_password("Special@Char") is False


def test_no_uppercase_letter_password() -> None:
    assert check_password("no@Upper1") is True


def test_too_long_password() -> None:
    assert check_password("TooLongPassw0rdWithSpeci@l123") is False


def test_should_check_min_length() -> None:
    assert check_password("Short!1") is False


def test_should_check_upper_letter() -> None:
    assert check_password("no@upper1") is False
