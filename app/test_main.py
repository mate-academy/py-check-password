from app.main import check_password


def test_check_minimum() -> None:
    assert check_password("Pass@w1") is False


def test_check_maximum() -> None:
    assert check_password("Pass@wd1234@D1123") is False


def test_ok_minimum() -> None:
    assert check_password("Pass@w1e") is True


def test_ok_maximum() -> None:
    assert check_password("Pass@wd1234@D112") is True


def test_number() -> None:
    assert check_password("Pass@wdr") is False


def test_symbol() -> None:
    assert check_password("Pass1wdr") is False


def test_letters() -> None:
    assert check_password("1234567@") is False
