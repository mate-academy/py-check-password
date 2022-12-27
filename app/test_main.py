from app.main import check_password


def test_is_too_long() -> None:
    assert check_password("mavdvPass@word1#423423r243fxsvAsv") is False


def test_is_all_lowercase() -> None:
    assert check_password("qw6!tdsvrerb") is False


def test_is_short() -> None:
    assert check_password("S@ng6") is False


def test_is_uppercase() -> None:
    assert check_password("JJCUVFMDE") is False


def test_for_special_symbols() -> None:
    assert check_password("DedMoroz666") is False


def test_without_digits() -> None:
    assert check_password("DedMoroz_lol#") is False
