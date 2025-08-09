from app.main import check_password


def test_correct_password() -> None:
    password_test = "Pass@word1"
    assert check_password(password_test) is True


def test_password_without_digits() -> None:
    password_test = "Pass@word"
    assert check_password(password_test) is False


def test_should_check_upper_letter() -> None:
    password_test = "pass@word"
    assert check_password(password_test) is False


def test_password_only_upper_letters() -> None:
    password_test = "PASS@WORD"
    assert check_password(password_test) is False


def test_password_without_special_symbols() -> None:
    password_test = "Password1"
    assert check_password(password_test) is False


def test_short_password() -> None:
    password_test = "Pass@1"
    assert check_password(password_test) is False


def test_long_password() -> None:
    password = "Pass@word1Pass@word2"
    assert check_password(password) is False


def test_empty_password() -> None:
    password = ""
    assert check_password(password) is False


def test_password_with_space() -> None:
    password = "Pass@word 1"
    assert check_password(password) is False
