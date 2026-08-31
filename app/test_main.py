from app.main import check_password


def test_check_password() -> None:
    assert check_password("Pass@word1") is True


def test_check_password_if_length_less_than_8() -> None:
    assert check_password("Short_1") is False


def test_check_password_if_length_more_than_18() -> None:
    assert check_password("Too_Long_password1") is False


def test_check_password_with_out_uppercase_letter() -> None:
    assert check_password("pass@word1") is False


def test_check_password_with_out_digit() -> None:
    assert check_password("Pass@word") is False


def test_check_password_with_out_special_character() -> None:
    assert check_password("Password1") is False
