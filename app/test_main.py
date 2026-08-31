import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Pass$@#&!-_34", True),
        pytest.param("$@#3&!PASS-_4", True),
        pytest.param("Pass$@#&!34+", False),
        pytest.param("pass$@#&!-_34", False),
        pytest.param("Password@#", False),
        pytest.param("Password234", False),
        pytest.param("Pass$84", False),
        pytest.param("Pass$_84", True),
        pytest.param("Pass$_8412344321!", False),
        pytest.param("", False)
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
