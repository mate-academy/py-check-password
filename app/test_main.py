import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "income_pass, expect_res",
    [
        ("Qwer#1", False),
        ("1Qwertyqwertyqwertyq#werty", False),
        ("qwerty12@", False),
        ("Qwerty123", False),
        ("Qwer#tyasda", False),
        ("Qw@rty123", True)
    ]
)
def test_check_password(income_pass: str, expect_res: str) -> None:
    assert check_password(income_pass) == expect_res
