from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_too_short_password() -> None:
    assert check_password("qwerty") is False


def test_no_special_character() -> None:
    assert check_password("Str0ngPass") is False


def test_no_digit() -> None:
    assert check_password("Special@Char") is False


def test_no_uppercase() -> None:
    assert check_password("lowercase@1") is False


def test_valid_minimum_length() -> None:
    assert check_password("Aa1$2") is False


def test_valid_maximum_length() -> None:
    assert check_password("Aa1$2Bb3@4Cc5-6") is True


def test_too_long_password() -> None:
    assert check_password("Aa1$2Bb3@4Cc5-6Dd7$8Ee9Ff0") is False


def test_invalid_characters() -> None:
    assert check_password("Invalid&Pass!") is False
