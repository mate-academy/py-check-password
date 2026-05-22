import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("", False),
        ("1", False),
        ("pass@word1", False),
        ("pass@word3333333333333312ergergergergterg54t3453453tg3gr3rg", False),
        ("Pass@word", False),
        ("Pass@", False),
        ("Password1", False),
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
