from app.main import check_password


def test_should_return_false_for_short_passwords() -> None:
    assert check_password("1@weW") is False


def test_should_return_false_for_long_passwords() -> None:
    assert check_password("qwerty12@Wfewfgrgdffds") is False


def test_should_return_false_for_password_without_digits() -> None:
    assert check_password("Qwerty@#QW") is False


def test_should_return_false_for_password_without_uppercase() -> None:
    assert check_password("qwe123@$qwe") is False


def test_should_return_false_for_password_without_spec_char() -> None:
    assert check_password("qwer123QWE") is False
