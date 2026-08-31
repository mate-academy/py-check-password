import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("Яasd32@sdf", False),
        ("ASd", False),
        ("ASdASdASdASdASdASd", False),
        ("Abcd12345", False),
        (",,,,,,,,,,", False),
        ("Abcd12345@", True)
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
