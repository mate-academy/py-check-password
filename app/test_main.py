# write your code here
from app.main import check_password


def test_without_upper() -> None:
    assert check_password("world@wordh1") is False


def test_password_without_digit() -> None:
    assert check_password("Pass@word") is False


def test_should_be_min_and_max_len() -> None:
    assert check_password("Tre1@") is False
    assert check_password("Rbhab3b8!8@knaeini@") is False


def test_should_contain_all_character() -> None:
    assert check_password("Pass@wld1we") is True
