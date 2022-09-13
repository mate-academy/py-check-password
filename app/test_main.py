from app.main import check_password


def test_at_least_8_characters():
    password = "P@word1"

    assert check_password(password) is False


def test_maximum_16_characters_inclusive():
    password = "Pass@word1Pass@wo"

    assert check_password(password) is False


def test_returns_false_for_passwords_without_digits():
    password = "Pass@word"

    assert check_password(password) is False


def test_returns_false_for_passwords_without_special_symbols():
    password = "Password1"

    assert check_password(password) is False


def test_returns_false_for_passwords_without_uppercase_letter():
    password = "ass@word1"

    assert check_password(password) is False


def test_contains_only_valid_characters():
    password = "Pass@w ord1"

    assert check_password(password) is False
