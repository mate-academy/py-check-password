from app.main import check_password


def test_check_password_min_len() -> None:
    assert check_password("Qwerty1@") is True  # 8 symbols
    assert check_password("Qwert1@") is False  # 7 symbols


def test_check_password_max_len() -> None:
    assert check_password("123456789Qwertyz@") is False  # 17 symbols
    assert check_password("123456789Qwerty@") is True  # 16 symbols


def test_check_password_numbers() -> None:
    assert check_password("Qwertyzxc@") is False  # without number
    assert check_password("1Qwertyzxc@") is True  # with number


def test_check_password_special_symbols() -> None:
    assert check_password("1Qwertyzxc") is False  # without special symbols
    assert check_password("1Qwertyzxc@") is True  # with special symbols


def test_check_password_uppercase_letter() -> None:
    assert check_password("1qwertyzxc@") is False  # without uppercase letter
    assert check_password("1Qwertyzxc@") is True  # with uppercase letter
