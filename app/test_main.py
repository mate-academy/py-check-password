import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Password1!", True),
        ("PASSWORD@2", True),
        ("password_1", False),
        ("Abcd#2", False),
        ("Qazxswedcvfrtgb-123", False),
        ("Password!", False),
        ("Password123", False),
        ("Password*1", False)
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
