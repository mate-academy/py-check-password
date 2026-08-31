import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("p@S1", False),
        ("pass_1_word", False),
        ("Password1", False),
        ("Pass@word1-Pass@word1", False),
        ("Pass@word", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
