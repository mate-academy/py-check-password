from app.main import check_password


def test_valid_password_min_length() -> None:
    assert check_password("A1@bcdef")


def test_valid_password_max_length() -> None:
    assert check_password("Abcdefghij1@KLMN")


def test_valid_password_with_all_requirements() -> None:
    assert check_password("Pass@word1")


def test_too_short_password() -> None:
    assert not check_password("A1@bcde")  # 7 символів


def test_too_long_password() -> None:
    assert not check_password("Abcdefghij1@KLMNO")  # 17 символів


def test_missing_uppercase() -> None:
    assert not check_password("password1@")


def test_missing_digit() -> None:
    assert not check_password("Password@")


def test_missing_special_symbol() -> None:
    assert not check_password("Password1")


def test_invalid_character() -> None:
    assert not check_password("Password1%")  # '%' не дозволений


def test_invalid_unicode() -> None:
    assert not check_password("Пароль1@")  # кирилиця


def test_invalid_space() -> None:
    assert not check_password("Pass word1@")  # пробіл


def test_empty_password() -> None:
    assert not check_password("")
