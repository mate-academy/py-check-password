from app.main import check_password


def test_password_to_short() -> None:
    assert check_password("Str@ng1") is False


def test_password_to_long() -> None:
    assert check_password("Str@ng1Str@ng1Str@ng") is False


def test_password_no_uppercase() -> None:
    assert check_password("str@ng1str@ng") is False


def test_password_no_digit() -> None:
    assert check_password("Str@ngStr@ng") is False


def test_password_no_special() -> None:
    assert check_password("Strong1Strong") is False


def test_password_forbidden_char() -> None:
    assert check_password("Str@ng1?Str@ng") is False


def test_password_ok() -> None:
    assert check_password("Pass@word1") is True
