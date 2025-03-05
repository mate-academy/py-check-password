import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Pass@word11111111", False),
        ("Password1", False),
        ("Pass@word", False),
        ("qwerty6@", False),
        ("qQ4&", False)
    ]
)
def test_should_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
