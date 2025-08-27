import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("passwor", False),
        ("passswwwwoooorrrrdddddd", False),
        ("Password123", False),
        ("Password_!", False),
        ("pass_@word", False),
        ("pass~word123z^", False),
        ("pass word", False),
        ("Пароль@198", False),
        # True passwords
        ("PassW_0rd", True),
        ("D@VeL0peRRR", True),
        ("Is_DeveL0Perrr!", True)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
