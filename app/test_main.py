from app.main import check_password


def test_valid_password_returns_true() -> None:
    result = check_password("Pass@word1")
    assert result


def test_too_short_password_returns_false() -> None:
    result = check_password("qwerty")
    assert not result


def test_too_long_password_returns_false() -> None:
    result = check_password("Qwerty1234567890!")
    assert not result


def test_password_without_digit_returns_false() -> None:
    result = check_password("Str@ng")
    assert not result


def test_password_with_invalid_char_returns_false() -> None:
    result = check_password("Hasło1@bc")
    assert not result


def test_password_without_uppercase_returns_false() -> None:
    result = check_password("password1@")
    assert not result


def test_password_without_special_char_returns_false() -> None:
    result = check_password("Password12")
    assert not result
