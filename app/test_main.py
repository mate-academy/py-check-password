from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_short_password() -> None:
    assert check_password("Pass@w1") is False


def test_long_password() -> None:
    assert check_password("12345678901234567890@Pp") is False


def test_no_uppercase_letter() -> None:
    assert check_password("password123@") is False


def test_no_digit() -> None:
    assert check_password("Pass@word") is False


def test_no_special_symbol() -> None:
    assert check_password("Password123") is False


def test_only_lowercase_letters() -> None:
    assert check_password("password") is False


def test_only_digits() -> None:
    assert check_password("1234567890") is False


def test_only_special_symbols() -> None:
    assert check_password("@#$%^&*()_+") is False


def test_repeating_characters() -> None:
    assert check_password("12321") is False
    assert check_password("Pass@word@word") is False
