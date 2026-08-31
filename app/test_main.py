import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Strong12345", False),
        ("strong@1234", False),
        ("Str@12", False),
        ("Str@ngIce", False),
        ("Str@ngIceMan123456789", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
