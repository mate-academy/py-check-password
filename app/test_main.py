from app.main import check_password


def test_for_true_password() -> None:
    assert check_password("Pass@word1")


def test_when_bed_password() -> None:
    assert not check_password("qwerty")


def test_without_a_capital_letter() -> None:
    assert not check_password("password_1")


def test_without_a_number() -> None:
    assert not check_password("Str@ngggggg")


def test_without_a_special_character() -> None:
    assert not check_password("Password1")


def test_less_than_8_characters() -> None:
    assert not check_password("Pass_1")


def test_more_than_16_characters() -> None:
    assert not check_password("ItismyPassword_11")


def test_misfits_characters() -> None:
    assert not check_password("Password_1++")


def test_when_only_numbers() -> None:
    assert not check_password("357348573")


def test_password_with_spaces() -> None:
    assert not check_password("Pass word_1")
