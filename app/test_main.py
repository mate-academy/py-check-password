import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="if password is valid"
        ),
        pytest.param(
            "Qwerty_123-qwerty",
            False,
            id="if password > 16 characters"
        ),
        pytest.param(
            "Str@ng1",
            False,
            id="if password < 8 characters"
        ),
        pytest.param(
            "password_1",
            False,
            id="id password doesn't have at least 1 uppercase letter."
        ),
        pytest.param(
            "Passw0rd",
            False,
            id="if password doesn't have at least 1 uppercase letter, "
               "and 1 special character"
        ),
        pytest.param(
            "P@ssword",
            False,
            id="if password doesn't have at least 1 digit, "
               "and 1 uppercase letter"
        ),
        pytest.param(
            "Пароль_1",
            False,
            id="if letter is non-Latin alphabet"
        )
    ]
)
def test_of_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
