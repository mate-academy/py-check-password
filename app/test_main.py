from app.main import check_password


def test_contains_letters_and_digits_and_special_character() -> None:
    assert check_password("Password123") is False
    assert check_password("P!ssword123") is True
    assert check_password("P@ssword") is False


def test_too_long_password() -> None:
    assert check_password("P@ssword123P@ssword123P@ssword123") is False
    assert check_password("P@ssword123P@ss") is True


def test_too_short_password() -> None:
    assert check_password("P@ss123") is False
    assert check_password("P@ssword123Pss!1") is True
