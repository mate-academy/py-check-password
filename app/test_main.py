import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Short1!", False),
        ("Too_loooooooooong1", False),
        ("NoSymbols2", False),
        ("no_uppercase1", False),
        ("No_digits", False),
    ]
)
def test_check_password_result(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
