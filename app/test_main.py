from app.main import check_password


def test_check_password_lower_then_eight_characters() -> None:
    assert check_password("Qwert-1") is False


def test_check_password_higher_then_sixteen_characters() -> None:
    assert check_password("Qwertyuiopasdfghj-1") is False


def test_no_uppercase_character() -> None:
    assert check_password("qwerty-1") is False


def test_no_digit() -> None:
    assert check_password("Qwerty-i") is False


def test_no_special_character() -> None:
    assert check_password("Qwertyu1") is False


def test_correct_password() -> None:
    assert check_password("Qwerty-1") is True
