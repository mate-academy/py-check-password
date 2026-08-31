import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        ("LongerPassword123!", False),
        ("NoSpecialChar123", False),
        ("NoDigit&Special", False),
        ("Pas_2", False),
        ("ppercaselett@4", False)
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
