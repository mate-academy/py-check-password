from app.main import check_password


def test_with_correct_name() -> None:
    password = "Pass@word1"
    assert check_password(password) is True


def test_without_upper_letters() -> None:
    password = "qwerty123@"
    assert check_password(password) is False


def test_without_digits() -> None:
    password = "Str@ngPass"
    assert check_password(password) is False


def test_with_too_long_password() -> None:
    password = "Str@ng12345678912345"
    assert check_password(password) is False


def test_with_too_short_password() -> None:
    password = "Pass@1"
    assert check_password(password) is False


def test_without_special_letters() -> None:
    password = "Password"
    assert check_password(password) is False
