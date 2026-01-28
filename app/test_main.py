from app.main import check_password


def test_check_password_long_password() -> None:
    assert check_password("Pass@wordbbbbqqqqqqqq15444qqqqqqqq") is False


def test_check_password_short_password() -> None:
    assert check_password("Qw@1") is False


def test_check_password_spec_symbol() -> None:
    assert check_password("Straaangaa1aa") is False


def test_check_password_not_digits() -> None:
    assert check_password("Qw@qqqqqqq") is False


def test_check_passwor_without_upper() -> None:
    assert check_password("ww@2wefcddd") is False


def test_true_password() -> None:
    assert check_password("Pass@word1") is True
