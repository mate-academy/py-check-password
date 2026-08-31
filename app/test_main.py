from app.main import check_password


def test_should_accept_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_should_check_upper_letter() -> None:
    assert check_password("qwertyu1@") is False


def test_should_check_max_length() -> None:
    assert check_password("Qwertyuiopasdfgh1@") is False


def test_should_check_min_length() -> None:
    assert check_password("Str0ng@") is False


def test_should_check_special_symbols() -> None:
    assert check_password("Password1") is False


def test_should_check_non_latin_alphabet() -> None:
    assert check_password("Пароль_1@") is False
