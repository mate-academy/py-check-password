import pytest

from app import main


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
    ],
)
def test_examples_from_task(password: str, expected: bool) -> None:
    assert main.check_password(password) is expected


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pas@wo1", False),
        ("Pass@wo1", True),
        ("Pass@word1Pass@w", True),
        ("Pass@word1Pass@wo", False),
        ("", False),
    ],
)
def test_password_length(password: str, expected: bool) -> None:
    assert main.check_password(password) is expected


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word",
        "Password1",
        "pass@word1",
    ],
)
def test_password_without_required_char(password: str) -> None:
    assert main.check_password(password) is False


@pytest.mark.parametrize("special", ["$", "@", "#", "&", "!", "-", "_"])
def test_every_allowed_special_char(special: str) -> None:
    assert main.check_password(f"Password1{special}") is True


@pytest.mark.parametrize(
    "password",
    [
        "Pass@word1 ",
        "Pass@word1%",
        "Pass@word1*",
        "Pąss@word1",
        "Pass@wordЖ1",
    ],
)
def test_not_allowed_chars(password: str) -> None:
    assert main.check_password(password) is False
