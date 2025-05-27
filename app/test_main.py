from .main import check_password
import pytest


@pytest.mark.parametrize(
    "password, value",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng1", False),
        ("Пароль123", False),
        ("Password12344543@", False),
        ("pass@word1", False),
        ("Password@", False)
    ],
    ids=["valid password",
         "No special, no upper letter",
         "Length password < 8",
         "No Latin letters",
         "Length password > 16",
         "No Upper letter",
         "No digits"],
)
def test_password(password: str, value: bool) -> None:
    assert check_password(password) == value
