import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Pass@word", False),
        ("Pass@r1", False),
        ("pass@word1", False),
        ("Pass@word1pass@word1", False),
        ("Password1", False),
        ("Mate_academy_1998065-+", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
