import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Abcdef1!",
            True
        ),
        pytest.param(
            "password",
            False,
            id="Should contain at least 1 digit, 1 "
               "special character, 1 uppercase letter"
        ),
        pytest.param(
            "Password",
            False,
            id="Should contain at least 1 digit, 1 "
               "special character, 1 uppercase letter"
        ),
        pytest.param(
            "Password!",
            False,
            id="Should contain at least 1 digit"
        ),
        pytest.param(
            "Password1",
            False,
            id="Should contain at least 1 special character"
        ),
        pytest.param(
            "Pass1!",
            False,
            id="Should be at least 8 characters long"
        ),
        pytest.param(
            "Password1!Password1!",
            False,
            id="Should be maximum 16 characters inclusive"
        ),
        pytest.param(
            "Пароль1234!",
            False,
            id="Should contain Latin alphabet Aa-Zz, digits 0-9 "
               "or symbols $@#&!-_"
        ),
        pytest.param(
            "Password1?",
            False,
            id="Should contain Latin alphabet Aa-Zz, digits 0-9 "
               "or symbols $@#&!-_"
        )
    ]
)
def test_check_password_requirements(password: str, expected: bool) -> None:
    assert check_password(password) == expected
