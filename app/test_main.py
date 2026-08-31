import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Pass@word1", True),
        ("Qwertydsf", False),
        ("sdfjjJj#2", True),
        ("qWerty12312fsDDdfgcxgsfadgfd###", False),
        ("pass##word1", False),
        ("PassWord!", False),
        ("2345@!A", False),
        ("ValidPass#1", True),
        ("NoDigit!", False),
        ("NoSpecial123", False),
    ],
)
def test_check_password(value: str, expected: bool) -> None:
    assert check_password(value) == expected
