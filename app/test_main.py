from app.main import check_password


def test_valid_password() -> None:
    # Meets all requirements: length 10, uppercase, digit, special char
    assert check_password("Pass@word1") is True


def test_length_boundaries() -> None:
    # 7 chars (too short)
    assert check_password("Ab1!def") is False
    # 8 chars (minimum valid)
    assert check_password("Ab1!defg") is True
    # 16 chars (maximum valid) - REMOVED THE LAST CHARACTER 'p'
    assert check_password("Ab1!defghijlkmno") is True
    # 17 chars (too long)
    assert check_password("Ab1!defghijlkmnop") is False


def test_missing_required_characters() -> None:
    # No digit
    assert check_password("Password!") is False
    # No special character
    assert check_password("Password123") is False
    # No uppercase
    assert check_password("pass@word1") is False


def test_disallowed_characters() -> None:
    # Contains space
    assert check_password("Pass @word1") is False
    # Contains non-Latin letter (e.g., Cyrillic or accented)
    assert check_password("Pass@wörd1") is False
    # Contains special char not in the allowed list (%)
    assert check_password("Pass%word1") is False


def test_empty_string() -> None:
    assert check_password("") is False
