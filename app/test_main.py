# write your code here
from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("P@1", False),
        ("Long@Password123456", False),
        ("Pass@OhneDigits", False),
        ("Pass1OhneSymbol", False),
        ("smallletters@5", False)
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert (
        check_password(password) == result
    ), "Result is not as expected"
