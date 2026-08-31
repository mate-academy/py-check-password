from app.main import check_password


def test_all_permitted_symbols() -> None:
    assert check_password("Abcdef$@123") is True


def test_shorter_then_min() -> None:
    assert check_password("Ab$@12") is False


def test_longer_then_max() -> None:
    assert check_password("Abcdefghqwertyuiopasdfghjkl$@123456789") is False


def test_without_digits() -> None:
    assert check_password("Abcdefg$@") is False


def test_without_upper_letters() -> None:
    assert check_password("abcde$@123") is False


def test_without_special_characters() -> None:
    assert check_password("Abcdefg1234") is False
