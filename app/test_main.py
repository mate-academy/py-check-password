import pytest
from app.main import check_password


@pytest.fixture()
def password_template() -> str:
    return "qweRt#3"


def test_check_len_password_short(password_template: str) -> None:
    assert check_password(password_template) is False


def test_check_len_password_long(password_template: str) -> None:
    password_template = "qweQWeqqqweyr33ty2#rr"
    assert check_password(password_template) is False


def test_check_has_upper(password_template: str) -> None:
    password_template = "qwerty2#rr"
    assert check_password(password_template) is False


def test_check_has_digit(password_template: str) -> None:
    password_template = "qwertySSS#"
    assert check_password(password_template) is False


def test_check_has_special(password_template: str) -> None:
    password_template = "qwertyW1rr"
    assert check_password(password_template) is False
