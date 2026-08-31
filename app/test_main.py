from app.main import check_password


def test_less_than_eight_chars_not_valid() -> None:
    assert check_password("Ab1!567") is False


def test_more_than_sixteen_chars_not_valid() -> None:
    assert check_password("Ab1!5678901234567") is False


def test_missing_special_character_not_valid() -> None:
    assert check_password("Ab1567890") is False


def test_missing_digit_not_valid() -> None:
    assert check_password("Abcdefghij!") is False


def test_missing_uppercase_character_not_valid() -> None:
    assert check_password("abcdefghij1!") is False


def test_valid_password() -> None:
    assert check_password("Abcdefghij1!") is True
