import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("hello", False),
        ("HelloMyFriend", False),
        ("H311oMyFr1end$!", True),
        ("H311oMyFr1end$!somanychar", False),
        ("maT34c4d3my", False),
        ("maT3_4c4d3my", True),
        ("Пароль228_", False),
        ("passw0rd_    ", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
