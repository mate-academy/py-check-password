import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("", False),
        ("Abcd1!s", False),
        ("Abcde!1fg22112eaA", False),
        ("ABCDabcd1", False),
        ("aaabbbccс1!", False),
        ("AAAbbbccc!", False),
        ("AAAбббссс1!", False),
        ("AAbcdef1!a", True)
    ],
    ids=[
        "test empty string",
        "test length password should be > 8 characters",
        "test length password should be < 16 characters",
        "test password should contain at least 1 special character",
        "test password should contain at least 1 digit",
        "test password should contain at least 1 uppercase letter",
        "test password should contain only Latin alphabet",
        "test valid password",
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
