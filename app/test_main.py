from app.main import check_password


def test_should_check_long_password():
    assert not check_password("a@dasdasdaS1dasdasdasda")


def test_should_check_short_of_password():
    assert not check_password("a@dd1A")


def test_should_check_up_symbol():
    assert not check_password("asccsd@1")


def test_should_check_special_symbol():
    assert not check_password("asccsdA1")


def test_should_check_number():
    assert not check_password("asccsd@A")
