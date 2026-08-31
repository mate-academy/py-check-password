import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Qwert1@", False),
        ("Qwertyuiopasdfgh&8", False),
        ("пес$патронF1", False),
        ("Superp@ssword#", False),
        ("iL0veYou", False),
        ("tiny-shiny00", False),
        ("Val!dGuy007", True),
    ],
    ids=[
        "return False if password less than 8 characters",
        "return False if password greater than 16 characters",
        "return False if password contains non-latin letters",
        "return False if password contains no digits",
        "return False if password contains no special characters",
        "return False if password contains no uppercase letter",
        "return True if all rules are met",
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
