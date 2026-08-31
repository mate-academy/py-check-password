from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True
    assert check_password("Qwer1@#$") is True
    assert check_password("Abc123!@#") is True


def test_invalid_password_length() -> None:
    assert check_password("Passw1@") is False  # Too short
    assert check_password("Pass@word12345678") is False  # Too long


def test_no_uppercase() -> None:
    assert check_password("pass@word1") is False


def test_no_digit() -> None:
    assert check_password("Password@") is False


def test_no_special_char() -> None:
    assert check_password("PasswordA1") is False


def test_invalid_characters() -> None:
    assert (check_password("Pass@word1*")
            is False)  # Contains "*" which is not allowed
    assert check_password("Пароль1@") is False  # Contains non-ASCII characters


def test_empty_password() -> None:
    assert check_password("") is False
