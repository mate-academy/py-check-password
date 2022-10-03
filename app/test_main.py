import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Password11@#&!-_", True,
            id="valid password"
        ),
        pytest.param(
            "Password10@#&!-_5", False,
            id="too long password"
        ),
        pytest.param(
            "Passw9@", False,
            id="too short password"
        ),
        pytest.param(
            "password11@", False,
            id="password without uppercase"
        ),
        pytest.param(
            "PASSWORD11@", True,
            id="password without lower case"
        ),
        pytest.param(
            "Password@", False,
            id="password without digits"
        ),
        pytest.param(
            "Password11", False,
            id="password without special character"
        ),
        pytest.param(
            "Password11*", False,
            id="password with unexpected special character"
        ),
    ]
)
def test_check_password(
        password: str,
        expected: bool,
):
    assert check_password(password) == expected
