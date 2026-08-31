import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Pass@word1", True, id="password is valid"),
        pytest.param("qW@ertdsdy", False, id="password has no digits"),
        pytest.param("ds2Fs@d", False, id="password is too short"),
        pytest.param("ds1@f22sd", False, id="password has no uppercase"),
        pytest.param(
            "dsfff22@dafasfaffAWREWRFsd",
            False,
            id="password is too long"
        ),
        pytest.param("ds2faffdFsd", False, id="password has no special chars"),
    ]
)
def test_password_validation(password: str, expected: bool) -> None:
    assert check_password(password) == expected
