from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Abc123$#") is True


def test_invalid_password_length() -> None:
    assert check_password("aBc1$") is False


def test_invalid_password_no_uppercase() -> None:
    assert check_password("abc123$#") is False


def test_invalid_password_no_digit() -> None:
    assert check_password("Abcdefgh$#") is False


def test_invalid_password_no_special_character() -> None:
    assert check_password("Abc1234567") is False


def test_invalid_password_false_when_pass_length_more_16() -> None:
    assert check_password("Password_BiggerThan16") is False
