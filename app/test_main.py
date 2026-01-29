import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("LongPassword@Password1", False),
        ("Pass@word", False),
        ("pass@word1", False),
        ("Word@1", False),
        ("Pass1word", False),
    ]
)
def test_valid_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
