import pytest

from app import main


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("1@Passwo", True),
        ("1@Password345678", True),
        ("PASS@WORD1", True),

        ("1@Passw", False),
        ("1@Password3456789", False),
        ("", False),

        ("Password123", False),
        ("Pass@word", False),
        ("pass@word1", False),

        ("Pass*word1", False),
        ("Pass word1", False),
        ("Pаss@word1", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert main.check_password(password) == expected
