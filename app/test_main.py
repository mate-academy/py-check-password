from app.main import check_password


def test_should_return_false_if_length_is_less_than_8():
    assert check_password("12Abc$") is False


def test_should_return_false_if_length_is_more_than_16():
    assert check_password("123456789Abcdefgh$") is False


def test_should_return_false_if_no_uppercase_letter():
    assert check_password("1234567abcdef$") is False


def test_should_return_false_no_digits_in_password():
    assert check_password("Abcdefghi$@") is False


def test_should_return_false_no_special_symbols_in_password():
    assert check_password("Abcdefghi123") is False


def test_should_true_for_correct_password():
    assert check_password("Abcdefghi123@") is True
