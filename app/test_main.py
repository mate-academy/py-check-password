import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, value",
    [
        ("Qwerty$@#&!-_1234", False),
        ("Qwer!3#", False),
        ("qwerty#7j", False),
        ("QwertY@uio_", False),
        ("Qwerty1235", False)
    ]
)
def test_check_password(
        password: str,
        value: bool
) -> None:
    assert check_password(password) == value
