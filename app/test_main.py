import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1234", True),
        ("Pass@word1", True),
        ("Pass_word1", True),
        ("Pass-word1", True),
        ("Pass@word123456789", False),
        ("password1@", False),
        ("Pass word1", False),
        ("PASSWORD@", False),
        ("Password1", False),
        ("P@ssw1A", False),
        ("qwerty", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
