# write your code here
import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_password, expected_result",
    [
        ("Password1@", True),
        ("Passw!1", False),
        ("Password123%", False),
        ("ABCDab!@#", False),
        ("abcdefgh123!", False),
        ("Abcdefgh1234$!!!!", False),
        ("Password123", False),
    ]
)
def test_check_password(
        input_password: str,
        expected_result: bool
) -> None:
    assert check_password(input_password) == expected_result
