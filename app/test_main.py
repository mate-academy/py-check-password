import pytest
import app.main as main


@pytest.mark.parametrize("pwd, expected", [
    ("Pass@word1", True),
    ("short1@", False),
    ("thisiswaytoolongpwd1@", False),
    ("Abcde1$2", True),
    ("AbcdefGh1$234567", True),
    ("NoDigit@A", False),
    ("nodigit1@", False),
    ("NoSpec123A", False),
    ("Has Space1@", False),
    ("Pass$word1", True),
])
def test_check_password(pwd: str, expected: bool) -> None:
    assert main.check_password(pwd) == expected


def test_too_long_password() -> None:
    assert main.check_password("AbcdefGh1$2345678") is False


def test_password_without_special() -> None:
    assert main.check_password("Password1") is False


def test_should_check_min_length() -> None:
    assert main.check_password("A1$aaaa") is False


def test_should_check_special_symbols() -> None:
    assert main.check_password("NoSpec123A") is False
