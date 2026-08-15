from app.main import check_password


def test_valid_password() -> None:
    assert check_password("Pass@word1") is True


def test_should_check_min_length() -> None:
    assert check_password("A@1bc") is False


def test_should_check_max_length() -> None:
    assert check_password("VeryL0ngP@ssword123") is False


def test_should_require_uppercase() -> None:
    assert check_password("password@1") is False


def test_should_require_digit() -> None:
    assert check_password("Password@") is False


def test_should_require_special_symbol() -> None:
    assert check_password("Password1") is False


def test_should_reject_invalid_symbol() -> None:
    assert check_password("Password1*") is False


def test_min_length_valid() -> None:
    assert check_password("Abcdef@1") is True


def test_max_length_valid() -> None:
    assert check_password("Abcdefghij@1234") is True


def test_another_valid_password() -> None:
    assert check_password("Good#Pass1") is True
