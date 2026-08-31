import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ngpassword", False),
        ("7843214", False),
        ("password", False),
        ("Password145", False),
        ("#%fas$fe4864#$#", False),
        ("парольвідакаунт", False),
        ("F@1se", False),
        ("MyP@ssword1488", True),
        ("Qwerty$15", True),
        ("TooLongP@ssword1598", False),
        ("password_1ower", False)
    ],
    ids=[
        "should return True as password is correct",
        "should return False as password lacks uppercase and digit",
        "should return False as password lacks digit",
        "should return False as password lacks uppercase and special",
        "should return False as password lacks uppercase, digit and special",
        "should return False as password lacks special and digit",
        "should return False as password lacks uppercase and digit",
        "should return False as password contains non-latin letters",
        "should return False as password is too short",
        "should return True as password is correct",
        "should return True as password is correct",
        "should return False as password is too long",
        "should return False as password lacks uppercase"
    ]
)
def test_checks_password_correctly(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
