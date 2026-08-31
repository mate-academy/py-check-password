import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expect_result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ngfdaf", False),
        ("Qwerty43", False),
        ("Ps@wd1", False),
        ("Psfdsfasdfdasfasdfds@wd1", False),
        ("qwer32@ty", False),
    ],
    ids=[
        "check valid password",
        "check if password with only lower case letters",
        "check if password without digits",
        "check if password without special symbols",
        "check if password is short",
        "check if password is too long",
        "check if password without uppercase letter"
    ]
)
def test_check_password(password: str, expect_result: bool) -> None:
    assert check_password(password) == expect_result
