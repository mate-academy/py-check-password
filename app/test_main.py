import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("", False),
        ("   ", False),
        ("Qwertyasdfgzxcvb12345!@#", False),
        ("Asd1!", False),
        ("asdfzxcvbqwer", False),
        ("123456789", False),
        ("!@#$!@#$!@#$", False),
        ("asdf1234!@#$", False),
        ("Asdf!@#$asdf", False),
        ("Asdf1234asdf", False),
        ("Asdf1234!@#$", True)
    ],
    ids=[
        "empty password",
        "spaces only",
        "above the range",
        "below the range",
        "lowercase only",
        "digits only",
        "special only",
        "no uppercase",
        "no digits",
        "no special",
        "correct one"
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
