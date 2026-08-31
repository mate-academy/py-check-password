from app.main import check_password


def test_valid_password() -> None:
    """Test valid password."""
    assert check_password("Pass@word1") is True


def test_short_password() -> None:
    """Test password shorter than 8 characters."""
    assert check_password("qwerty") is False


def test_long_password() -> None:
    """Test password longer than 16 characters."""
    assert check_password("A1@bcdefghijklmnopq") is False


def test_no_digit() -> None:
    """Test password without digits."""
    assert check_password("Pass@word") is False


def test_no_special_char() -> None:
    """Test password without special characters."""
    assert check_password("Password1") is False


def test_no_uppercase() -> None:
    """Test password without uppercase letters."""
    assert check_password("pass@word1") is False


def test_invalid_characters() -> None:
    """Test password with invalid characters."""
    assert check_password("Пароль123!") is False


def test_min_length() -> None:
    """Test password with minimum length (8 characters)."""
    assert check_password("A1@bcdef") is True


def test_max_length() -> None:
    """Test password with maximum length (16 characters)."""
    assert check_password("A1@bcdefghijklmn") is True


def test_empty_password() -> None:
    """Test empty password."""
    assert check_password("") is False


def test_only_lowercase() -> None:
    """Test password with only lowercase letters."""
    assert check_password("password") is False


def test_only_uppercase() -> None:
    """Test password with only uppercase letters."""
    assert check_password("PASSWORD") is False


def test_only_digits() -> None:
    """Test password with only digits."""
    assert check_password("12345678") is False


def test_only_special_chars() -> None:
    """Test password with only special characters."""
    assert check_password("@#$%^&*") is False


def test_missing_one_requirement() -> None:
    """Test password missing one requirement (e.g., no uppercase)."""
    assert check_password("pass@word1") is False


def test_all_requirements_met() -> None:
    """Test password meeting all requirements."""
    assert check_password("Pass@word1") is True
