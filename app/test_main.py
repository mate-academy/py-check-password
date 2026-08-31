import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("WOrd!1", False),
        ("password", False),
        ("12345678", False),
        ("!@#$######", False),
        ("PASSWORD", False),
        ("password123", False),
        ("PaSsWoRd123", False),
        ("PAssWord@@@", False),
        ("password123###", False),
        ("PASSWORD123###", True),
        ("1234567890Word$$_", False),
        ("Password123$$", True),
        ("1234567890Word$$", True),

    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
