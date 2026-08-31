import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expect_result",
    [
        pytest.param(
            "Qwer!y1", False, id="length of password less than 8 characters"
        ),
        pytest.param(
            "Qwertyqwertyqwer!1",
            False,
            id="length of password more than 16 characters"
        ),
        pytest.param(
            "Passw@rd",
            False,
            id="password should contain at least one digit"
        ),
        pytest.param(
            "pa$$w0rd",
            False,
            id="password should contain at least one Capital letter"
        ),
        pytest.param(
            "Passw0rd",
            False,
            id="password should contain at least one special character"
        ),
        pytest.param(
            "Pa$$w0rd",
            True,
            id="password should contains at least 1 digit, "
               "1 special character, 1 uppercase letter"
        ),
    ]
)
def test_check_password(password: str,
                        expect_result: bool) -> None:
    assert check_password(password) is expect_result
