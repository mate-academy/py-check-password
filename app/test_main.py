import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "example, expected",
    [
        ("Z_1", False),
        ("Z_1211111111111111111111111", False),
        ("abcd_1234", False),
        ("aBcd_Abcd", False),
        ("abcD1234", False),
        ("Abcd_1234", True),
    ]
)
def test_check_password(example: str, expected: bool) -> None:
    assert expected == check_password(example)
