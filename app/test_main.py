import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Short1!", False),
        ("ThisIsWayTooLong1!", False),
        ("password1!", False),
        ("Password!", False),
        ("Password1", False),
        ("Password1*", False),
        ("Пароль1!#", False),
        ("Strong_Pass1!", True)
    ]
)
def test_check_all_validators(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
