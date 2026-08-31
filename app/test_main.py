from app.main import check_password


def test_amount_characters_more_then_sixteen() -> None:
    assert check_password("Pass@word1assdfggd") is False


def test_password_without_digits() -> None:
    assert check_password("Pass@worda") is False


def test_password_without_uppercase() -> None:
    assert check_password("pas@sword1") is False


def test_password_short_password() -> None:
    assert check_password("Pa@1") is False
