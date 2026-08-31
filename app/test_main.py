from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("qwe@tY3") is False


def test_returns_false_for_too_long_passwords() -> None:
    assert check_password("Q1@ascdsadfghjklb") is False


def test_non_valid_password() -> None:
    assert check_password("Str@ng") is False


def test_at_least_1_digit() -> None:
    assert check_password("Stong@Password") is False


def test_at_least_1_special() -> None:
    assert check_password("StongPassword1") is False


def test_at_least_1_upper() -> None:
    assert check_password("stongpassword@1") is False


def test_max_16_characters() -> None:
    assert check_password("1Q@qwertyuikjhgf") is True


def test_min_8_characters() -> None:
    assert check_password("ABcD12@#") is True


def test_invalid_password() -> None:
    assert check_password("mama") is False


def test_invalid_character_space() -> None:
    assert check_password("Pass word1@") is False


def test_other_characters() -> None:
    assert check_password("żółtek@A1") is False


def test_short_password_only_length_issue() -> None:
    assert check_password("A1@aBcD") is False
