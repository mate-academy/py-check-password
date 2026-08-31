import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("123", False),
        ("12345678", False),
        ("abcdefgh", False),
        ("Abcdefgh", False),
        ("Abcdefg0", False),
        ("Abcdefg0$", True),
        ("Abcdefghijklmno0$", False),
        ("A0$", False),
        ("abcdefg0$", False),
        ("Abcdefg$", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert (check_password(password) == result)
