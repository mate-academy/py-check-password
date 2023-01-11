import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("qwerty@1", False),
        ("Qwert@1", False),
        ("Qwerty@12311233123", False),
        ("Qwerty$2", True),
        ("Qwertyu22", False),
        ("Passwor@", False),
    ]
)
def test_check_password(
        password: str,
        result: bool) -> None:
    assert check_password(password) == result
