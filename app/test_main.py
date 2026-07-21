from app.main import check_password


def test_valid_password() -> None:
    assert check_password(
        "Pass@word1"
    ) is True


def test_password_less_than_eight() -> None:
    assert check_password(
        "Ab1@xyz"
    ) is False


def test_password_more_than_sixteen() -> None:
    assert check_password(
        "Abcdefghijklmnop1@"
    ) is False


def test_password_without_uppercase() -> None:
    assert check_password(
        "password@1"
    ) is False


def test_password_without_digit() -> None:
    assert check_password(
        "Password@"
    ) is False


def test_password_without_special_symbol() -> None:
    assert check_password(
        "Password1"
    ) is False


def test_password_with_space() -> None:
    assert check_password(
        "Pass word1@"
    ) is False


def test_password_with_forbidden_symbol() -> None:
    assert check_password(
        "Pass%word1"
    ) is False


def test_password_with_allowed_special_symbols() -> None:
    assert check_password(
        "Strong#1"
    ) is True


def test_password_min_length() -> None:
    assert check_password(
        "Ab1@cdef"
    ) is True


def test_password_max_length() -> None:
    assert check_password(
        "Abbbbbbbbbbbb1@"
    ) is True
