from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,expected_output",
    [
        ("Pass@word1", True),
        ("Pass@w1", False),
        ("Pass@word1toolong", False),
        ("pass@word1", False),
        ("Pass@word!", False),
        ("Pass1word2", False)
    ]
)
def test_check_password(
        password: str,
        expected_output: bool
) -> None:
    assert check_password(password) == expected_output
