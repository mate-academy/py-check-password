from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_only_letters_invalid() -> None:
    assert check_password("qwerty") is False


def test_too_short() -> None:
    assert check_password("Str@ng") is False


def test_too_long() -> None:
    assert check_password("A1@" + "a" * 20) is False


def test_missing_uppercase() -> None:
    assert check_password("password1@") is False


def test_missing_digit() -> None:
    assert check_password("Password@") is False


def test_missing_special() -> None:
    assert check_password("Password1") is False


def test_invalid_character_polish_letter() -> None:
    assert check_password("Passąword1@") is False


def test_invalid_character_other_symbol() -> None:
    assert check_password("Pass?word1") is False
