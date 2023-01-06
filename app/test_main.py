from app.main import check_password


def test_existing_8_characters() -> None:
    assert check_password("1@D") is False


def test_existing_maximum_16_characters() -> None:
    assert check_password("1@Dewfgaw4rtgbg56nb") is False


def test_existing_1_digit() -> None:
    assert check_password("Q@wertyoki") is False


def test_existing_1_special_character() -> None:
    assert check_password("1Qwertyok") is False


def test_existing_1_uppercase_letter() -> None:
    assert check_password("1@qwertyok") is False
