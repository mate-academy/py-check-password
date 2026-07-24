import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("Pass@wo1", True),
        ("Pass@word12345_1", True),
        ("Pass@wo", False),
        ("Pass@word123456_1", False),
        ("Pass@word", False),
        ("Passw0rd1", False),
        ("pass@word1", False),
        ("Pass%word1", False),
        ("Pass word1", False),
        ("Pass@wordЯ1", False),
        ("", False),
        ("qwerty", False),
        ("Str@ng", False),
    ],
    ids=[
        "valid password with all required characters",
        "valid password with minimum length of eight",
        "valid password with maximum length of sixteen",
        "too short password with seven characters",
        "too long password with seventeen characters",
        "password without digit",
        "password without special character",
        "password without uppercase letter",
        "password with forbidden special character",
        "password with whitespace",
        "password with non latin letter",
        "empty password",
        "short password without required characters",
        "short password with special character",
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected, (
        f"check_password('{password}') should return {expected}"
    )


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "Pass#word1",
        "Pass&word1",
        "Pass!word1",
        "Pass-word1",
        "Pass_word1",
        "Pass$word1",
    ],
    ids=[
        "at sign is allowed",
        "hash sign is allowed",
        "ampersand is allowed",
        "exclamation mark is allowed",
        "hyphen is allowed",
        "underscore is allowed",
        "dollar sign is allowed",
    ],
)
def test_all_allowed_special_characters(password: str) -> None:
    assert check_password(password) is True, (
        f"check_password('{password}') should return True"
    )


def test_should_return_bool() -> None:
    assert isinstance(check_password("Pass@word1"), bool), (
        "Function should return a boolean value"
    )
