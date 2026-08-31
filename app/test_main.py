import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("pass@word1", False),
        ("Password1", False),
        ("Pass@word", False),
        ("Pass@word123456789", False),
        ("", False),
        ("P@s1", False)
    ],
    ids=[
        "Correct password",
        "Upper case is missing",
        "Special char is missing",
        "Digit is missing",
        "Password longer than 16 chars",
        "Password fild is empty",
        "Password is to short"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    ), f"This password {password} has to give {result}"
