import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "example, expected",
    [
        ("A_1", False),
        ("A_1211111111111111111111111", False),
        ("abcd_1234", False),
        ("abcd_Abcd", False),
        ("abcD1234", False),
        ("Abcd_1234", True),
    ]
)
def test_check_password(example: str, expected: bool) -> None:
    assert expected == check_password(example)
