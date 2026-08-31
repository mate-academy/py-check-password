import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("qwerty", False),
        ("Str@ng", False),
        ("Q2@rty", False),
        ("qwertyqwert2@Yqwerty", False),
        ("Q@ertyqwerty", False),
        ("F3rrtyqwerty", False),
        ("Pass@word1", True),
        ("приввет43#&Q", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
