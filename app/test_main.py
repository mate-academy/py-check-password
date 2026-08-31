from app.main import check_password


def test_length_below_required() -> None:
    assert not check_password("Dimas6#")
    assert not check_password("A1!")


def test_length_above_required() -> None:
    assert not check_password("Dimasfkarabas666#")


def test_password_composition_is_full() -> None:
    assert check_password("Dimas96#")
    assert not check_password("Dimas1996")
    assert not check_password("Ronaldinho!!!")
    assert not check_password("poroshenko55!")
    assert not check_password("vasyapetrov")


def test_not_latin_letter_should_be_not_approved() -> None:
    assert not check_password("ЫDimas96#")


def test_appropriate_passwords() -> None:
    assert check_password("Dimas96#")
    assert check_password("$Taras01")
    assert check_password("P@nas238")
    assert check_password("&&&vodolaZ45")
    assert check_password("sibaZZ66!")
    assert check_password("1987Messi-boh")
    assert check_password("Penald0_loh")


def test_password_is_complete_with_not_allowed_symbols() -> None:
    assert not check_password("1987Messi/boh$")
    assert not check_password("Ilove_you100500?")
