from app.main import check_password


def test_strong_password() -> None:
    assert check_password("Pass@word1") is True


def test_short_password() -> None:
    assert check_password("k01A$$") is False


def test_long_password() -> None:
    assert check_password("Parol#7655493457395395785") is False


def test_password_without_numbers() -> None:
    assert check_password("Edikedik_$") is False


def test_password_without_upper() -> None:
    assert check_password("pss#word1108") is False


def test_password_without_symbols() -> None:
    assert check_password("Password1999") is False
