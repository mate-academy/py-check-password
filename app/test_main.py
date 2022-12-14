from app.main import check_password


def test_password_less_then_8_characters() -> None:
    assert not check_password("Kilo72!")


def test_password_more_then_16_characters() -> None:
    assert not check_password("Kilo72!Mega90_Gig")


def test_password_contains_at_least_1_required_character() -> None:
    assert check_password("Kilo172!")


def test_password_accepts_only_designetad_characters() -> None:
    assert not check_password("Kilo:72")


def test_password_requires_uppercase_letters() -> None:
    assert not check_password("password24!")


def test_password_requires_special_symbol() -> None:
    assert not check_password("Password24")


def test_password_requires_at_least_one_digit() -> None:
    assert not check_password("Password!")
