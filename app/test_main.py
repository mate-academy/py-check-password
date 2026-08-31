from app.main import check_password


all_special_characters = "$@#&!-"
special_character = "#"
number = "9"
too_many_letters = "QWERTYUIOPLKJHGFDSAZXCVBNM"
capital_letter = "G"
some_6_lower_letters = "qwerty"
some_5_lower_letters = "qwert"


def test_false_if_less_than_8_characters() -> None:
    password = special_character + number + capital_letter
    assert check_password(password) is False


def test_true_if_have_exactly_8_characters() -> None:
    password = (special_character
                + number
                + capital_letter
                + some_5_lower_letters)
    assert check_password(password) is True


def test_true_if_have_exactly_16_characters() -> None:
    password = (
        special_character
        + number
        + capital_letter
        + some_5_lower_letters
    ) * 2
    assert check_password(password) is True


def test_false_if_more_than_16_characters() -> None:
    password = special_character + number + capital_letter + too_many_letters
    assert check_password(password) is False


def test_false_if_there_is_no_any_number() -> None:
    password = special_character + capital_letter + some_6_lower_letters
    assert check_password(password) is False


def test_false_if_there_is_no_any_capital_letter() -> None:
    password = special_character + number + some_6_lower_letters
    assert check_password(password) is False


def test_false_if_there_is_no_any_special_character() -> None:
    password = number + capital_letter + some_6_lower_letters
    assert check_password(password) is False


def test_true_all_allowed_special_characters() -> None:
    password = all_special_characters + number + capital_letter
    assert check_password(password) is True
