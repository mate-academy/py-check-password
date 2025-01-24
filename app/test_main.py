import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected", [
        ("pass@word1", False),
        ("pass@word1", False),
        ("Pass@w1", False),
        ("Pass@wwwwwwwwwww1", False),
        ("Passxword1", False),
        ("Pass@wordx", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
