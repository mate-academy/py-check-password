from app.main import check_password


def test_strong_password():
    assert check_password("Pass@word1") is True


def test_short_password():
    assert check_password("Qwert@1") is False


def test_long_password():
    assert check_password("Str@ngqwert12345679@#") is False


def test_password_without_digits():
    assert check_password("Qwe@rtyqwerty") is False


def test_password_without_upper():
    assert check_password("pass@word123") is False


def test_password_without_symbols():
    assert check_password("Strong123") is False
