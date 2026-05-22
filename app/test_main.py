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
        ("Pass@word", False),
        ("Password1", False),
        ("Pass@1", False),
        ("Passw@r1", True),
        ("Passwordd123@AA", True),
        ("Passworddd123@AA", False)
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
