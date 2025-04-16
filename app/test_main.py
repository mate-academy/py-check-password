import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("@1Pq", False),
        ("@1PPPdjlaffsdflasdjf", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password1", False),
        ("Pass@word1", True)
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
