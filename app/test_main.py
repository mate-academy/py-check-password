import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("A123!bhh", True),
        ("A123!bfyfdhmlugl", True),
        ("A123!bh", False),
        ("A123!bfyfdhmluglh", False),
        ("A123bhhh", False),
        ("123!bhhh", False),
        ("gii#Abhj", False),
        ("123!4567", False),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
