from app.main import check_password


def test_should_check_min_length() -> None:
    assert check_password("S@1a") is False  # Too short


def test_should_check_max_length() -> None:
    assert check_password("A@1" + "x" * 20) is False  # Too long


def test_should_check_upper_letter() -> None:
    assert check_password("lower@1word") is False  # No uppercase


def test_should_check_digit() -> None:
    assert check_password("NoDigits@") is False  # No digits


def test_should_check_special_symbols() -> None:
    assert check_password("NoSpecial1") is False  # No special characters


def test_should_accept_valid_password() -> None:
    assert check_password("Val1d@Pass") is True  # Meets all criteria
