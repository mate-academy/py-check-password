import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        # happy path
        ("Pass@word1", True),
        ("P@sswo1d", True),
        ("Pass@word1234567", True),
        # boundary cases
        ("P@sswo1", False),
        ("Pass@word12345678", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password123", False),
        ("Pass%word1", False),
        ("Pass @word1", False),
        ("Páss@word1", False)
    ]
)
def test_check_password_functionality(password: str, expected: bool) -> None:
    assert check_password(password) == expected
