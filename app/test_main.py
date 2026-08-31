import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Paswo_1", False,
                     id="'False', when short passwords"),
        pytest.param("1234567890@Qwertyu", False,
                     id="'False', when too long passwords"),
        pytest.param("password_13", False,
                     id="'False', when no uppercase letter"),
        pytest.param("Password13", False,
                     id="'False', when no special character"),
        pytest.param("Password_aa", False,
                     id="'False', when no digit")
    ]
)
def test_check(password: str, expected: bool) -> None:
    assert check_password(password) == expected
