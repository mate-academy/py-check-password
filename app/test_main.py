from app.main import check_password


def test_return_false_when_pass_length_less_8() -> None:
    assert check_password("Aloha8!") is False


def test_return_false_when_pass_length_more_17() -> None:
    assert check_password("Password_has_more_than_17_digits!") is False


def test_return_true_when_pass_is_good_enough() -> None:
    assert check_password("P@ssword1") is True


def test_return_false_when_pass_has_not_digit() -> None:
    assert check_password("P@ssword") is False


def test_return_false_when_pass_has_not_upper_letter() -> None:
    assert check_password("p@ssword1") is False


def test_return_false_when_pass_has_not_special_char() -> None:
    assert check_password("Password1") is False
