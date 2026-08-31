import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_output",
    [
        ("Pa1!", False),
        ("Passwd1!", True),
        ("Password1!", True),
        ("Passsssssssswd1!", True),
        ("Passsssssssssssswd1!", False),
    ],
    ids=[
        "Password length < 8",
        "Password length = 8",
        "Password 8 < length < 16",
        "Password length = 16",
        "Password length > 16",
    ]
)
def test_check_password_length(password: str, expected_output: bool) -> None:
    assert check_password(password) == expected_output


@pytest.mark.parametrize(
    "password, expected_output",
    [
        ("!Password", False),
        ("!Password1", True),
    ],
    ids=[
        "Password without digits",
        "Password with digits",
    ]
)
def test_check_password_digits(password: str, expected_output: bool) -> None:
    assert check_password(password) == expected_output


@pytest.mark.parametrize(
    "password, expected_output",
    [
        ("!1password", False),
        ("!1Password", True),
    ],
    ids=[
        "Password without uppercase letters",
        "Password with uppercase letters",
    ]
)
def test_check_password_uppercase(password: str,
                                  expected_output: bool) -> None:
    assert check_password(password) == expected_output


@pytest.mark.parametrize(
    "password, expected_output",
    [
        ("1Password", False),
        ("|1Password", False),
        ("!1Password", True),

    ],
    ids=[
        "Password without special characters",
        "Password with unallowed special character",
        "Password with allowed special characters",
    ]
)
def test_check_password_special_character(password: str,
                                          expected_output: bool) -> None:
    assert check_password(password) == expected_output
