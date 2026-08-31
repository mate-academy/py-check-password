from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result", [
        ("Dola23@", False),
        ("Кирилиця№1", False),
        ("MyPasswordIsSooCool@#55", False),
        ("superpass_33", False),
        ("MyPassword123", False),
        ("restorDru#_", False),
        ("Dola$raN89", True)
    ],
    ids=[
        "Password is too short (at least 8 symbols)",
        "Accepts only latin alphabet",
        "Password is too long (>16 symbols)",
        "Should contain at least one uppercase letter",
        "Should contain at least one special symbol",
        "Should contain at least one digit",
        "Should return true if requirements is accomplished"
    ]
)
def test_passwords(password: str, result: bool) -> None:
    assert check_password(password) == result
