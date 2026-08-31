from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_password_is_short() -> None:
    assert check_password("P1@ssor") is False


def test_password_is_long() -> None:
    assert check_password("Passqwwei1@oeriorefnnfsdjfdsnsdj") is False


def test_password_without_digit() -> None:
    assert check_password("Pass@word") is False


def test_password_without_special_char() -> None:
    assert check_password("Password1") is False


def test_password_without_uppercase() -> None:
    assert check_password("pas1@wordpassw") is False
