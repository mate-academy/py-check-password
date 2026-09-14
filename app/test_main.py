from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_short_password() -> None:
    assert check_password("Str@ng") is False


def test_no_uppercase() -> None:
    assert check_password("pass@word1") is False


def test_no_digit() -> None:
    assert check_password("Pass@word") is False


def test_no_special_character() -> None:
    assert check_password("Password1") is False


def test_invalid_character() -> None:
    assert check_password("Pass@word1*") is False


def test_too_long_password() -> None:
    assert check_password("Pass@word12345678") is False


def test_min_length() -> None:
    assert check_password("A1@bcde") is False


def test_max_length() -> None:
    assert check_password("A1@bcdefghijklmn") is True


def test_exactly_7_characters() -> None:
    assert check_password("A1@bcde") is False


def test_exactly_17_characters() -> None:
    assert check_password("A1@bcdefghijklmnop") is False
