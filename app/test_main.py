import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Numb$r3",
            False,
            id="Minimum length check"
        ),
        pytest.param(
            "NoNumber$",
            False,
            id="Digit check"
        ),
        pytest.param(
            "ThisIs@VeryLong1Password",  # більше 16 символів
            False,
            id="Check max length"
        ),
        pytest.param(
            "Number33",
            False,
            id="Special character check"
        ),
        pytest.param(
            "numb$r33",
            False,
            id="Check for capitalization"
        ),
        pytest.param(
            "Pass@word1",  # правильний пароль
            True,
            id="Valid password"
        )
    ]
)
def test_check_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected
