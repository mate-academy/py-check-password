from app.main import check_password


def test_check_length_password_short() -> None:
    assert check_password("Pa@wo1") is False


def test_check_password_normal() -> None:
    assert check_password("Pa@woasd1")


def test_check_none_uppercase_letter() -> None:
    assert check_password("pa@woasd1") is False


def test_check_long_length() -> None:
    assert check_password("Pa@woasd1asdfgw#a") is False


def test_check_none_special_character() -> None:
    assert check_password("Paswoasd1") is False


def test_check_none_digit() -> None:
    assert check_password("Pa@woasdhg") is False
