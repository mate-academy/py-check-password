from app.main import check_password


def test_password_too_short() -> None:
    """Ensure passwords shorter than the minimum length are rejected."""
    assert not check_password("Ab&1")


def test_password_no_uppercase() -> None:
    """Ensure passwords without uppercase letters are rejected."""
    assert not check_password("ab1de$fgh")


def test_password_no_lowercase() -> None:
    """Ensure passwords without lowercase letters are rejected."""
    assert not check_password("ASB1$ET")


def test_password_with_invalid_character() -> None:
    """Ensure passwords with invalid characters are rejected."""
    assert not check_password("kndK*NKE8")


def test_password_too_long() -> None:
    """Ensure passwords longer than the maximum length are rejected."""
    assert not check_password("Ab1de$fghijklmnop")


def test_password_with_not_special_character() -> None:
    """Ensure passwords without special characters are rejected."""
    assert not check_password("Ab1defgh")


def test_password_with_not_digit() -> None:
    """Ensure passwords without digits are rejected."""
    assert not check_password("Abcdef$g")
