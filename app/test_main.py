from app.main import check_password


def test_correct_password() -> None:
    assert check_password("Pass@word1") is True


def test_without_uppercase_letter() -> None:
    assert check_password("password!8") is False


def test_without_digit() -> None:
    assert check_password("Password@") is False


def test_without_special_character() -> None:
    assert check_password("Password3") is False


def test_more_than_16_characters() -> None:
    assert check_password("Pass@word1qwerty9") is False


def test_less_than_8_characters() -> None:
    assert check_password("qwrtY@8") is False


def test_empty_password() -> None:
    assert check_password("") is False
