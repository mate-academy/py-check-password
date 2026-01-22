import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        (
            "Pass@word1", True
        ),
        (
            "short1!", False
        ),
        (
            "Password@", False
        ),
        (
            "password@1", False
        ),
        (
            "Password1", False
        ),
        (
            "Password@1*", False
        ),
        (
            "Pass@1wo", True
        ),
        (
            "Password@12word1", True
        ),
        (
            "Pass*1!o", False
        ),
        (
            "Password@1*word1", False
        )
    ]
)
def test_check_password(password: str, expected: str) -> None:
    assert check_password(password) == expected


def test_password_too_short() -> None:
    assert check_password("A1@a") is False


def test_password_too_long() -> None:
    password = "Password@1" + "a" * 10
    assert check_password(password) is False
