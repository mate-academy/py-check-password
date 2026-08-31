from app.main import check_password


def test_return_false_short():
    assert check_password("1d#F") is False


def test_return_false_long():
    assert check_password("12F#ds34567890asd1234567") is False


def test_return_false_no_digit():
    assert check_password("Qwertyu#") is False


def test_return_false_no_upper():
    assert check_password("4wertyu#") is False


def test_return_false_no_symbol():
    assert check_password("4wQertyu") is False


def test_return_false_other_symbol():
    assert check_password("4wQe*rtyu") is False


def test_return_true_all_correct():
    assert check_password("4wQerty#u") is True
