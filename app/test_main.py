import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Password1", False),
        ("password1!", False),
        ("Password!", False),
        ("Sh0rt!", False),
        ("to0lonGpassword!!", False),
        ("two words", False)
    ],
    ids=[
        "correct password",
        "no special symbols",
        "no upper case",
        "no digits",
        "too short",
        "too long",
        "password with spaces"
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
