from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1")


def test_valid_minimum_length() -> None:
    assert not check_password("Aa0@Bb1")


def test_valid_maximum_length() -> None:
    assert not check_password("LongPass@word123456")


def test_invalid_length_too_short() -> None:
    assert not check_password("Short!1")


def test_invalid_length_too_long() -> None:
    assert not check_password("ExceedsMaxLength@1_234567")


def test_invalid_no_digit() -> None:
    assert not check_password("NoDigitSpecial@")


def test_invalid_no_special_character() -> None:
    assert not check_password("NoSpecial123456")


def test_invalid_no_uppercase() -> None:
    assert not check_password("noupp3r@special")


def test_invalid_invalid_character() -> None:
    assert not check_password("Invalid$Pa$$word1")


def test_invalid_empty_password() -> None:
    assert not check_password("")


def test_invalid_space_in_password() -> None:
    assert not check_password("Space In@Pass")
