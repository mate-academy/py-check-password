import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("pass@word1", False),
        ("PASSWORD@1", True),
        ("Password1", False),
        ("P@ssword1", True),
        ("Pa$$w0rd12345678", True),
        ("Pa$$w0rd123456789", False),
        ("Pass^word1", False),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
