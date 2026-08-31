import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("p@ssw0rd", False),
        ("P@ass5", False),
        ("Secre1pass", False),
        ("Qw#e$rty_", False),
        ("P@ssw0rd135791135", False),
    ],
    ids=[
        "Password without uppercase letter (A-Z).",
        "Password is too short(at least 8 characters).",
        "Password without special character ($@#&!-_).",
        "Password without digits (1-9).",
        "Password is too long maximum 16 characters inclusive."
    ]
)
def test_check_password_function(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
