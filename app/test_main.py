import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "test_password, expected_result",
    [
        ("Qwertyyy$", False),
        ("Qw12$", False),
        ("Qwerty1234567890$", False),
        ("qwerty123$", False),
    ]
)
def test_check_password(test_password: str, expected_result: bool) -> None:
    assert check_password(test_password) == expected_result
