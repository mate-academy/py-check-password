from app.main import check_password


def test_should_check_upper_letter() -> None:
    assert check_password("password_1") is False


def test_should_check_digit() -> None:
    assert check_password("Password_") is False


def test_should_check_special_symbols() -> None:
    assert check_password("Password1") is False


def test_should_check_min_length() -> None:
    assert check_password("Pass_1") is False


def test_should_check_max_length() -> None:
    assert check_password("Passwordpassword_12") is False
