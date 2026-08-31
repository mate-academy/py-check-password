from app.main import check_password


def test_should_return_false_for_password_without_digits() -> bool:
    assert check_password("P@ssword") is False


def test_should_return_false_for_too_long_password() -> bool:
    assert check_password("P@ssword1234567890") is False


def test_should_return_false_for_too_short_password() -> bool:
    assert check_password("Qwe1@") is False


def test_should_return_false_for_password_without_special_symbols() -> bool:
    assert check_password("Password1") is False


def test_should_return_false_for_password_without_uppercase_latter() -> bool:
    assert check_password("p@ssword1") is False
