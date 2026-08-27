import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Password1@", True),
        ("Pass@wor", False),
        ("Pass@word1234567", True),
        ("pass@word1", False),
        ("PASSWORD@", False),
        ("Password@", False),
        ("Password1", False),
        ("Pass word1@", False),
        ("Пасword1@", False),
        ("Pass.word1@", False),
    ]
)
def test_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
