from app.main import check_password


def test_return_false_when_no_special_character():
    assert not check_password("1234Test")


def test_return_false_when_no_uppercase_letter():
    assert not check_password("1234@@test")


def test_return_false_when_no_digits():
    assert not check_password("Testpwd@@ss")


def test_return_false_when_shorter_then_8():
    assert not check_password("14@@Pwd")


def test_return_false_when_longer_then_16():
    assert not check_password("142222222222@@Pwd")
