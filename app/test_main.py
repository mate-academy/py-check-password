from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short() -> None:
    assert check_password("Str@ng1") is False


def test_min_length_boundary() -> None:
    assert check_password("Abcdef1@") is True


def test_max_length_boundary() -> None:
    assert check_password("Abcdefghij1@Klm") is True


def test_too_long() -> None:
    assert check_password("Abcdefghij1@Klmno") is False


def test_no_uppercase() -> None:
    assert check_password("password1@") is False


def test_no_digit() -> None:
    assert check_password("Password@") is False


def test_no_special_character() -> None:
    assert check_password("Password1") is False


def test_invalid_character() -> None:
    assert check_password("Pass word1@") is False


def test_invalid_special_character() -> None:
    assert check_password("Password1*") is False
