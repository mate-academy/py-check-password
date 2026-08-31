from app.main import check_password


def test_strong_password():
    assert check_password("Pass@word1") is True


def test_short_password():
    assert check_password("P@ss1") is False


def test_long_password():
    assert check_password("Pass@word12345678") is False


def test_password_without_numbers():
    assert check_password("Pass@word") is False


def test_password_without_upper():
    assert check_password("pass@word1") is False


def test_password_without_symbols():
    assert check_password("Password1") is False
