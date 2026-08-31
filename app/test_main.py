from app.main import check_password


def test_check_password_valid() -> None:
    assert check_password("Pass@word1") is True


def test_check_password_too_short() -> None:
    assert check_password("Str@ng") is False  # 6 characters
    assert check_password("S@1") is False     # 3 characters
    assert check_password("") is False        # Empty password


def test_check_password_too_long() -> None:
    assert check_password("VeryL0ngPassw@rd_123") is False


def test_check_password_no_digit() -> None:
    assert check_password("Password@") is False


def test_check_password_no_special() -> None:
    assert check_password("Password1") is False


def test_check_password_no_uppercase() -> None:
    assert check_password("pass@word1") is False


def test_check_password_invalid_character() -> None:
    assert check_password("Passw@rd1^") is False


def test_check_password_exact_minimum() -> None:
    assert check_password("P@ssw0rd") is True


def test_check_password_exact_maximum() -> None:
    assert check_password("P@ssw0rd123456") is True


def test_check_password_only_specials_and_digits() -> None:
    assert check_password("1234@#") is False
