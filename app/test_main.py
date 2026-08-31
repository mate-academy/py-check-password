from app.main import check_password


def test_check_valid_password() -> None:
    password = "Pass@word1"
    assert check_password(password) is True


def test_check_qwerty_password() -> None:
    password = "qwerty"
    assert check_password(password) is False


def test_check_simple_password() -> None:
    password = "Str@ng"
    assert check_password(password) is False


def test_check_8_character_password() -> None:
    password = "Str@nge3"
    assert check_password(password) is True


def test_check_7_character_password() -> None:
    password = "Str@nge"
    assert check_password(password) is False


def test_check_16_character_password() -> None:
    password = "xK9$vL2!mP7@bN5&"
    assert check_password(password) is True


def test_check_17_character_password() -> None:
    password = "xK9$vL2!mP7@bN5&4"
    assert check_password(password) is False


def test_check_password_without_number() -> None:
    password = "Str@nged"
    assert check_password(password) is False


def test_check_password_without_capital_letter() -> None:
    password = "$@#&!-p12345"
    assert check_password(password) is False


def test_check_password_without_symbol() -> None:
    password = "Str9noed"
    assert check_password(password) is False


def test_check_password_with_cyrillic() -> None:
    password = "Str@ngeл2"
    assert check_password(password) is False


def test_check_password_with_space() -> None:
    password = "Str@S tr@nge3"
    assert check_password(password) is False
