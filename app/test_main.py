import pytest
from app.main import check_password


@pytest.fixture
def valid_password() -> None:
    return "Pass@word1"


@pytest.fixture
def invalid_short_password() -> None:
    return "P@word1"


@pytest.fixture
def invalid_long_password() -> None:
    return "Str@ngLongPassword123"


@pytest.fixture
def passwords_without_uppercase_letter() -> None:
    return "pass@word1"


@pytest.fixture
def no_special_char() -> None:
    return "NoDi1Special"


@pytest.fixture
def no_digits() -> None:
    return "No_cialChar"


def test_valid_password(valid_password: any) -> None:
    assert check_password(valid_password)


def test_invalid_short_password(invalid_short_password: any) -> None:
    assert not check_password(invalid_short_password)


def test_invalid_long_password(invalid_long_password: any) -> None:
    assert not check_password(invalid_long_password)


def test_passwords_without_uppercase_letter(
        passwords_without_uppercase_letter: any
) -> None:
    assert not check_password(passwords_without_uppercase_letter)


def test_no_special_char(no_special_char: any) -> None:
    assert not check_password(no_special_char)


def test_no_digits(no_digits: any) -> None:
    assert not check_password(no_digits)
