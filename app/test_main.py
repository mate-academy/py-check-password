import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("QwertyQwerty", False),
        ("12345678", False),
        ("!@!@!!@!", False),
        ("Qwerty123", False),
        ("231234!@#", False),
        ("Qwer1!", False),
        ("TooLongPassword@!1", False),
        ("NoDigits!", False),
        ("Qwerty22!", True)
    ],
    ids=[
        "Only letters",
        "Only digits",
        "Only special chars",
        "Letters and digits",
        "Digits and special char",
        "Not enough length",
        "Too long password",
        "Without digits",
        "Valid password"
    ]
)
def test_outdated_products(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
