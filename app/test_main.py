from app.main import check_password


def test_should_return_false_if_password_too_short() -> None:
    assert check_password("qwerty1") is False


def test_should_return_false_if_password_too_long() -> None:
    assert check_password("qwertytworty25123") is False


def test_should_return_false_if_no_digit() -> None:
    assert check_password("Qwerties@") is False


def test_should_return_false_if_no_special_char() -> None:
    assert check_password("Qwerties1") is False


def test_should_return_false_if_no_uppercase_letter() -> None:
    assert check_password("qwerties#1") is False


def test_should_return_false_if_no_latin_letter() -> None:
    assert check_password("Qwerties#1ц") is False


def should_return_true_if_meets_all_condition_test() -> None:
    assert check_password("Pass@word1") is True
