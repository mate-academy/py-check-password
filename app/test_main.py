import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("привіт43#&Q", False),
        ("Q2@rty", False),
        ("qwertyqwert2@Yqwerty", False),
        ("Q@ertyqwerty", False),
        ("F3rrtyqwerty", False),
        ("Pass@word1", True),

    ],
    ids=[
        "check for allowed chars",
        "check for at least 8 characters",
        "check for 16 characters exclusive",
        "check contains digit,",
        "check contains special symbols",
        "everything OK!",
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
