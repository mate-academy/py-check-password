from app.main import check_password


def test_if_les_then_8_characters() -> None:
    len_pass = "Str@n1"
    result = check_password(len_pass)

    assert result is False


def test_if_more_then_16_characters() -> None:
    len_pass = "Str@ngdfa5fa41dhfg7"
    result = check_password(len_pass)

    assert result is False


def test_if_only_lowercase_characters() -> None:
    len_pass = "qwerty@1"
    result = check_password(len_pass)

    assert result is False


def test_if_all_uppercase_characters() -> None:
    len_pass = "QWERTY@"
    result = check_password(len_pass)

    assert result is False


def test_on_special_characters() -> None:
    len_pass = "Password1"
    result = check_password(len_pass)

    assert result is False


def test_on_numbers_characters() -> None:
    len_pass = "Pass@word"
    result = check_password(len_pass)

    assert result is False


def test_if_all_characters_is_fine() -> None:
    len_pass = "Pass@word1"
    result = check_password(len_pass)

    assert result is True
