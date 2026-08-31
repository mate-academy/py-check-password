from app.main import check_password


def test_check_password_ok_1() -> bool:
    assert check_password("a5sswordu@") is False


def test_check_password_ok_2() -> bool:
    assert check_password("df5dfgO$ydjtyjdyjryjryj") is False


def test_check_password_ok_3() -> bool:
    assert check_password("P5ass#") is False


def test_check_password4() -> bool:
    assert check_password("Pas@sword") is False


def test_check_password5() -> bool:
    assert check_password("Password111") is False
