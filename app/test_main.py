from app.main import check_password


def test_with_digit_special_char_upper_len_10() -> None:
    assert check_password("Pass@word1")


def test_less_than_8_characters() -> None:
    assert check_password("P@3") is False


def test_with_8_characters() -> None:
    assert check_password("P@ssw0rd") is True


def test_more_than_16_characters() -> None:
    assert check_password("Superp@ssword1234") is False


def test_with_16_characters() -> None:
    assert check_password("Superp@ssword123") is True


def test_only_lower_case_letters() -> None:
    assert check_password("p@ssw0rd") is False


def test_without_special_characters() -> None:
    assert check_password("Passw0rd") is False


def test_without_digits() -> None:
    assert check_password("P@ssword") is False


def test_with_whitespace() -> None:
    assert check_password("P@ss w0rd") is False


def test_only_uppercase_letters() -> None:
    assert check_password("P@SSW0RD") is True
