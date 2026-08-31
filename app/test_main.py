import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("password123$", False),
        ("PASSWORD123$", True),
        ("PassWord$", False),
        ("Pass1word", False),
        ("P@1", False),
        ("P@ssw0rd123456789", False),
        ("Valid-123$", True),
        ("Inv@lid?", False),
        ("Pa$$w0rd", True),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
