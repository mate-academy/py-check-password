from app.main import check_password


def test_must_be_at_least_8_characters_long() -> None:
    assert not check_password("1@Anywo")


def test_must_be_no_more_than_16_characters_length() -> None:
    assert not check_password("1@Anywords1@Anywo")


def test_password_must_have_at_least_1_digits() -> None:
    assert not check_password("@Anywords")


def test_password_must_have_at_least_1_special_character() -> None:
    assert not check_password("1Anywords")


def test_password_must_have_at_least_1_uppercase_letter() -> None:
    assert not check_password("1@anywords")


def test_password_must_pass_all_verifications() -> None:
    assert check_password("1@Anywords")
