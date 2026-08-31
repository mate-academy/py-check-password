import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("Passw!1", False),
        ("Password123%", False),
        ("фімав123!*$3", False),
        ("ABCDab!@#", False),
        ("abcdefgh123!", False),
        ("Abcdefgh1234$!!!!", False),
        ("Password123", False),
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
