from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, check",
    [
        ("Pass@word1", True),
        ("p@ssword0", False),
        ("Passw0rd", False),
        ("P@ssw0rd_P@ssw0rd", False),
        ("P@ssword", False),
        ("P@ssw0", False),
    ]
)
def test_check_password_with_all_parametrize(
        password: str,
        check: bool
) -> None:
    assert check_password(password) == check
