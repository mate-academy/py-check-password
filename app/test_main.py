from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Sh0rt@", False),
        ("VeryLongPass@word1", False),
        ("noupperpass@1", False),
        ("Pass@worд1?", False),
        ("Pass@word!", False),
        ("Password123", False)
    ],
    ids=[
        "Should return True for valid password",
        "Should return False for short password",
        "Should return False for too long password",
        "Should return False for password without uppercase",
        "Should return False for password with not allowed characters",
        "Should return False for password without numbers",
        "Should return False for password without special characters"
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
