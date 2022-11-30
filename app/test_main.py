from app.main import check_password


def test_short_password_income() -> None:
    assert check_password("!888bM") is False


def test_long_password_income() -> None:
    assert check_password("!888bMpeppaPigisGreat") is False


def test_password_without_uppercase_letter() -> None:
    assert check_password("!888bm7777") is False


def test_password_without_digits() -> None:
    assert check_password("!Bmwbmwmercedes") is False


def test_password_without_special_symbols() -> None:
    assert check_password("888bMgreat") is False
