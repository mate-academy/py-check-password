from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_valid_password_with_all_special_chars() -> None:
    assert check_password("Val!d@123-") is True


def test_valid_max_length() -> None:
    assert check_password("Abcdefghij@1234") is True  # length 16


def test_valid_min_length() -> None:
    assert check_password("A1@bcdef") is True  # length 8


def test_too_short_password() -> None:
    assert check_password("A1@bcde") is False  # length 7


def test_too_long_password() -> None:
    assert check_password("A1@bcdefghijklmnop") is False  # length 17


def test_missing_uppercase() -> None:
    assert check_password("password1@") is False


def test_missing_digit() -> None:
    assert check_password("Password@") is False


def test_missing_special_char() -> None:
    assert check_password("Password1") is False


def test_invalid_character_non_latin() -> None:
    assert check_password("Pässword1@") is False  # "ä" is not allowed


def test_invalid_character_special() -> None:
    assert check_password("Password1*") is False  # "*" is not allowed


def test_empty_password() -> None:
    assert check_password("") is False
