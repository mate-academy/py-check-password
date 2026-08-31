from app.main import check_password


def test_checkpassword_3_characters_invalid() -> None:
    password = "P@1"
    assert check_password(password) is False


def test_check_password_17_characters_invalid() -> None:
    password = "P1ssssswwwww@@@@@"
    assert check_password(password) is False


def test_check_password_16_characters_valid() -> None:
    password = "P1ssssswwwww@@@@"
    assert check_password(password) is True


def test_check_password_8_characters_valid() -> None:
    password = "P1ss@ssw"
    assert check_password(password) is True


def test_check_password_10_characters_valid() -> None:
    password = "P1ss@sswTT"
    assert check_password(password) is True


def test_check_password_no_uppercase_letters_invalid() -> None:
    password = "p1ss@ssw"
    assert check_password(password) is False


def test_check_password_no_digits_invalid() -> None:
    password = "Psss@ssw"
    assert check_password(password) is False


def test_check_password_no_special_characters_invalid() -> None:
    password = "P1ssTssw"
    assert check_password(password) is False


def test_check_password_cyrillic_letter_invalid() -> None:
    password = "P1ss@Дssw"
    assert check_password(password) is False
