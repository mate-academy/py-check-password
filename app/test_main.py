import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("123@Ab78", True),
        ("1234#Am890klM&jh", True),
        ("123@Ab7", False),
        ("1234#Am890klM&ja7", False),
        ("123fAb78", False),
        ("123@ab78", False),
        ("klo@Abhj", False),
        ("123@5678", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
