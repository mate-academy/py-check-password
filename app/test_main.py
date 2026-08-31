import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "abcdefg1$",
    "LongPass1234567890"
    "OnlyLowercaseletters@",
    "Short1$",
    "Password123",
    "Strong@Password",
])
def test_invalid_password(password: str) -> None:
    assert check_password(password) is False
