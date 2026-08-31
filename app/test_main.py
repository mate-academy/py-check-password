import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, validity",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Too_long_password1", False),
        ("no_capital_let", False),
        ("No_spec_char", False),
        ("1Small!", False),
        ("Пароль123!", False)

    ]

)
def test_check_password(password: str, validity: bool) -> None:
    assert check_password(password) == validity
