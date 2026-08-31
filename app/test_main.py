import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password_to_check,result",
    [
        ("Pass@d1", False),
        ("Pass@word12345675", False),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
    ],
    ids=[
        "should have at least 8 characters",
        "should have maximum 16 characters inclusive",
        "should contain at least one digit",
        "should contain at least one special caharacter",
        "should contain at least one uppercase letter",
    ]
)
def test_check_password(
    password_to_check: str,
    result: bool
) -> None:
    assert check_password(password_to_check) is result
