import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("Pass@word1", True),
        ("Pass@1", False),
        ("Passw@r1", True),
        ("Passwordd123@AA", True),  # 16 chars
        ("Passwordddd123@AA", False),  # 17 chars
        ("password1@", False),
        ("Password@", False),
        ("Password1", False),
        ("Password1*", False),
        ("", False),
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
