from app.main import check_password


def test_long_password() -> None:
    result = check_password("Lil8ponijifjeifjiej!ifjie")
    assert result is False


def test_have_upper() -> None:
    result = check_password("fehhfieh32!")
    assert result is False


def test_have_digit() -> None:
    result = check_password("Fehfhihe!")
    assert result is False


def test_have_special_symbols() -> None:
    result = check_password("Nifil9if")
    assert result is False


def test_without_letters() -> None:
    result = check_password("6!*44__*")
    assert result is False


def test_short_password() -> None:
    result = check_password("6H!ller")
    assert result is False
