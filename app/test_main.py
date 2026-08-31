from app.main import check_password


def test_returns_true_for_valid_password() -> None:
    result = check_password("Pass@word1")
    assert result is True


def test_returns_false_is_less_than_8_characters() -> None:
    result = check_password("Pa@d1")
    assert result is False


def test_returns_false_if_cyrillic_letter() -> None:
    result = check_password("Pфss@word1")
    assert result is False


def test_returns_false_if_too_many_characters() -> None:
    result = check_password("Pass@word11234567")
    assert result is False


def test_returns_false_if_doesnt_contain_digit() -> None:
    result = check_password("Pass@word")
    assert result is False


def test_returns_false_if_doesnt_contain_special_char() -> None:
    result = check_password("Password1")
    assert result is False


def test_returns_false_if_doesnt_contain_uppercase_letter() -> None:
    result = check_password("pass@word1")
    assert result is False
