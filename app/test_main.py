import pytest

from app import main


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1",
        "Abcdef1!",
        "A1@bcdef",
        "A1@bcdefghijklmn",
        "Password1$",
        "Password1@",
        "Password1#",
        "Password1&",
        "Password1!",
        "Password1-",
        "Password1_",
    ],
)
def test_valid_password(password: str) -> None:
    assert main.check_password(password) is True


@pytest.mark.parametrize(
    "password",
    [
        "A1@bcde",
        "A1@bcdefghijklmno",
        "qwerty",
        "Str@ng",
        "password1!",
        "PASSWORD@",
        "Password1",
    ],
)
def test_invalid_password_requirements(password: str) -> None:
    assert main.check_password(password) is False


@pytest.mark.parametrize(
    "password",
    [
        "Password1%",
        "Password1*",
        "Password1+",
        "Password1 ",
        "Password1.",
        "Password1/",
        "Password1А",
    ],
)
def test_password_with_forbidden_characters(password: str) -> None:
    assert main.check_password(password) is False
