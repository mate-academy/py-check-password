from app.main import check_password


def test_should_return_false_if_password_is_empty() -> None:
    assert check_password("") is False


def test_should_return_false_if_password_is_less_then_eight_chars() -> None:
    assert check_password("Pas@wd1") is False


def test_should_return_false_if_password_is_more_then_sixteen_chars() -> None:
    assert check_password("Paaaaaaaaaaas@wd1") is False


def test_should_return_false_if_password_has_not_uppercase() -> None:
    assert check_password("pass@word1") is False


def test_should_return_false_if_password_has_not_special_character() -> None:
    assert check_password("Password1") is False


def test_should_return_false_if_password_has_not_digit() -> None:
    assert check_password("Pass@word") is False


def test_should_return_true_if_password_has_not_lowercase_letters() -> None:
    assert check_password("PASS@@@@WORD112") is True


# def test_should_return_false_if_password_has_nolatin_char() -> None:
#     assert check_password("Pass@woцrd1") is False


def test_should_return_bool() -> None:
    assert isinstance(check_password("Pass@woцrd1"), bool)
