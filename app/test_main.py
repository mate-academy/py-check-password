from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, confirm",
    [
        ("asdf", False),
        ("asdAAD@@f", False),
        ("a48577$#@sdf", False),
        ("aA4@", False),
        ("1234567890DGGHTgfkhlsh@#$dlkgj", False),
        ("aAAdfhg4345@", True)
    ]
)
def test_check_password(
    password: str,
    confirm: bool
) -> None:
    assert check_password(password) == confirm
