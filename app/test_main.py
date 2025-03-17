import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        ("pass1word#", False),
        ("Qwer7type", False),
        ("St1r@ng", False),
        ("q1w@Aertsdcsdnfgdcnaxc", False),
        ("Bomberm@n", False)
    ]
)
def test_is_the_password_being_checked_correctly(
    password: str, is_valid: bool
) -> None:
    assert check_password(password) == is_valid
