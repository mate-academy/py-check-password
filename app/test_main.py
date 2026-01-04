import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Password2", False),
        ("qwerty#4", False),
        ("Str@ng2", False),
        ("", False),
        ("Tyijh$12ss0!zxAxcs", False),
        ("Insid@erS", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
