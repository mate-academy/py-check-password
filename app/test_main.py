from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("11ooo#", False),
        ("TooLongPass@1Aa!!", False),
        ("Has Space1!", False),
        ("Śpecial1@", False),

    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
