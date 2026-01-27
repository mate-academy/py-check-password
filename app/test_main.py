from app.main import check_password


def test_should_check_upper() -> None:
    assert check_password("password1$") is False


def test_should_check_digits() -> None:
    assert check_password("Password$") is False


def test_should_check_special() -> None:
    assert check_password("Password1") is False


def test_should_check_less_then_8() -> None:
    assert check_password("P1$a") is False


def test_should_check_more_then_16() -> None:
    assert check_password("Password1$aaaaaaa") is False
