import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pswrd1!",
            False,
            id="test less than 8 characters"
        ),
        pytest.param(
            "Password12345!&#_-",
            False,
            id="test more than 8 characters"
        ),
        pytest.param(
            "password123!",
            False,
            id="test without uppercase letter"
        ),
        pytest.param(
            "Password#&",
            False,
            id="test without digit"
        ),
        pytest.param(
            "Password890",
            False,
            id="test without special character"
        ),
        pytest.param(
            "Пароль_1234",
            False,
            id="test with not Latin alphabet"
        ),
        pytest.param(
            "Password333@/",
            False,
            id="test with another special character"
        ),
        pytest.param(
            "",
            False,
            id="test empty string"
        ),
        pytest.param(
            "Correct_pass1!",
            True,
            id="test correct password"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
