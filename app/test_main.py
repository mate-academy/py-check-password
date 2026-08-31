import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "expected_password,expected_result",
    [
        ("Pyt&0n", False),
        ("My!project", False),
        ("helloworld", False),
        ("paasswordPassw@r1", False),
        ("Pass@word1", True),
        ("aaaaaaa1&", False)
    ]
)
def test_check_password(
        expected_password: str,
        expected_result: bool
) -> None:
    assert check_password(expected_password) == expected_result
