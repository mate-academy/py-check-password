import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "initial_password,password_is_valid",
    [
        ("Pass@word1", True),
        ("Qw@rt1", False),
        ("Str@ngpass", False),
        ("p@ssw0rd", False),
        ("Passw0rd", False),
        ("To0LongP@ssw00rdd", False),
    ],
    ids=[
        "Password should be valid "
        "if it has at least 1 digit, "
        "1 special character, "
        "1 uppercase letter and "
        "length rather equal than 8",
        "Password should has length rather equal than 8",
        "Password should has at least 1 digit",
        "Password should has at least 1 uppercase letter",
        "Password should has at least 1 special character",
        "Password should has length less equal than 16",
    ]
)
def test_check_password_work_correctly(
        initial_password: str,
        password_is_valid: bool
) -> None:
    assert check_password(password=initial_password) == password_is_valid
