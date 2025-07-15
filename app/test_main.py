import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("aA1@", False),
        ("aA1@aA1@aA1@aA1@aA1@", False),
        ("a1@aa1@aa1@a", False),
        ("Aa1aAa1aAa1a", False),
        ("aA@aaA@aaA@a", False),
        ("aA1@aA1@aA1@", True),
        ("aA1@aA1@", True),
        ("aA1@aA1@aA1@aA1@", True),
    ],
    ids=[
        "too short password",
        "too long password",
        "without upper",
        "without special character",
        "without digit",
        "medium password",
        "exactly 8 characters",
        "exactly 16 characters"
    ]
)
def test_check_password(
    password: str,
    expected: bool
) -> None:
    assert check_password(password) is expected