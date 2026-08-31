from app.main import check_password


def test_short_password() -> None:
    assert check_password("Pa@rd1") is False


def test_too_long_password() -> None:
    assert check_password("Pass@word11111111") is False


def test_without_upper_case() -> None:
    assert check_password("pass@word1") is False


def test_check_digits() -> None:
    assert check_password("Pass@wordd") is False


def test_check_special_symbol() -> None:
    assert check_password("Passsword1") is False
