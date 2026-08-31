from app.main import check_password


def test_check_password_min_8_characters():
    assert check_password("a1!Za") is False


def test_check_password_max_18_characters():
    assert check_password("a1!Za111100000000000") is False


def test_check_password_not_upper_letter():
    assert check_password("a!1xabcd") is False


def test_check_password_not_digits():
    assert check_password("ax!Zabcd") is False


def test_check_password_not_special_character():
    assert check_password("a1xZabcd") is False


def test_check_password_all_correct():
    assert check_password("a1!Zabcd") is True
