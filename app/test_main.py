import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@word1", True,
            id="Valid password must be True"
        ),
        pytest.param(
            "qwerty", False,
            id="Password should contain at least 1 uppercase letter"
        ),
        pytest.param(
            "Str@ng", False,
            id="Password should contain at least 1 digit"
        ),
        pytest.param(
            "Password", False,
            id="Password should contain at least 1 special character"
        ),
        pytest.param(
            "q@3", False,
            id="Password should contain at least 8 characters"
        ),
        pytest.param(
            "Pass@wordddddddddddddddddddddddd1", False,
            id="Maximum 16 characters inclusive"
        ),
        pytest.param(
            "Пароль1@", False,
            id="Accepts only letters of the Latin alphabet"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
