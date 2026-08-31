from app.main import check_password


def test_min_password_length() -> None:
    assert not check_password("Pass@11")


def test_max_password_length() -> None:
    assert not check_password("P@ssword123_P@ss1")


def test_contains_special_characters() -> None:
    assert not check_password("Password1")


def test_password_contains_digits() -> None:
    assert not check_password("P@ssword")


def test_password_contains_uppercase() -> None:
    assert not check_password("p@ssword123_")
