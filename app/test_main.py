import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, except_pass",
    [
        ("Qwertyyy$", False),
        ("Qw12$", False),
        ("Qwerty1234567890$", False),
        ("qwerty123$", False),
    ],
)
def test_check_password(password: str, except_pass: bool) -> None:
    assert check_password(password) == except_pass
