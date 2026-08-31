import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="accepts only letters of the Latin alphabet Aa-Zz, "
               "digits 0-9 or special character"
        ),
        pytest.param(
            "Password_123456789@",
            False,
            id="should have maximum 16 elements"
        ),
        pytest.param(
            "qwerty",
            False,
            id="should have minimum 8 elements"
        ),
        pytest.param(
            "Str@ng",
            False,
            id="contains at least  1 special character"
        ),
        pytest.param(
            "Passworg_1",
            True,
            id="contains at least 1 digit, "
               "1 special character, 1 uppercase letter"
        ),
        pytest.param(
            "Worдцs_123",
            False,
            id="accepts only letters of the Latin alphabet Aa-Zz"
        ),
    ]
)
def test_check_password_correctly(
        password: str,
        result: bool
) -> None:

    assert check_password(password) == result
