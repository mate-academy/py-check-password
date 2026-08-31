import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ["123Qwer@ty456", True],
        ["QWEruUip1", False],
        ["QWEruUip!", False],
        ["qwertyuo!@#123", False],
        ["1Qq!", False],
        ["NBZ123RR!T", True],
        ["k123", False],
        ["Pass@word1", True],
        ["Pass@word12345678", False]
    ]
)
def test_passing_my_passwords(
        password: str,
        expected: bool
) -> bool:
    assert check_password(password) == expected
