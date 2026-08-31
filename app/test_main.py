from app.main import check_password


def test_if_no_special_symbols() -> None:
    assert check_password("String12345") is False


def test_if_no_upper_symbols() -> None:
    assert check_password("string14@32") is False


def test_if_no_digits() -> None:
    assert check_password("Str@ing!!!") is False


def test_if_too_many_symbols() -> None:
    assert check_password("Str3434!@sdgr!@!@#dgfgr") is False


def test_if_not_enough_symbols() -> None:
    assert check_password("Str1!") is False
