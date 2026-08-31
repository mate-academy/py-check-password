# write your code here
import pytest
from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1")
    assert check_password("Valid$123")
    assert check_password("A1b2C3d4!")


def test_invalid_password_length() -> None:
    assert not check_password("Short1!")
    assert not check_password("ThisPasswordIsWayTooLong123!")


def test_invalid_password_no_uppercase() -> None:
    assert not check_password("password1!")


def test_invalid_password_no_digit() -> None:
    assert not check_password("Password!")


def test_invalid_password_no_special_char() -> None:
    assert not check_password("Password1")


def test_invalid_password_invalid_chars() -> None:
    assert check_password("Password1!@#")


def test_empty_password() -> None:
    assert not check_password("")


if __name__ == "__main__":
    pytest.main()
