from app.main import check_password


def test_should_return_false_if_password_less_8_letters():
    assert check_password("1Dss$") is False


def test_should_return_false_if_password_more_16_letters():
    assert check_password("1Dsrtf6dg#jfhhjfhhs$") is False


def test_should_return_true_if_password_is_correcting():
    assert check_password("1Dsfkophs$") is True


def test_return_false_if_passwords_without_uppercase_letter():
    assert check_password("1sfkophs$") is False


def test_return_false_if_passwords_without_uppercase_digits():
    assert check_password("sfDkophs$") is False


def test_return_false_if_passwords_without_uppercase_simbols():
    assert check_password("sfGDkophs") is False
