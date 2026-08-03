import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "test_password, expected",
    [
        ("1Qwertyuiopasdfghjklzxcvbnm_", False),
        ("1Qwert!", False),
        ("Qwertyuiop!", False),
        ("Qwertyuio1", False),
        ("qwertyuio1_", False),
        ("1Qwertyui!", True)
    ]
)
def test_check_password(test_password: str, expected: bool) -> None:
    result = check_password(test_password)
    assert result == expected, f"Expected {expected}, got {result}"
