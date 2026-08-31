import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Password1",
            False,
            id="Password doesn't contain a special character."
        ),
        pytest.param(
            "password1@",
            False,
            id="Password doesn't have uppercase letter."
        ),
        pytest.param(
            "Password@",
            False,
            id="Password doesn't contain a digit"
        ),
        pytest.param(
            "Pass1@",
            False,
            id="Password's length should have at least 8 characters"
        ),
        pytest.param(
            "Password1@Password1@",
            False,
            id="Password's length should have less than 16 characters"
        ),
        pytest.param(
            "Пасворд:)",
            False,
            id="Password accepts only letters of the Latin alphabet"
        ),
        pytest.param(
            "Password1@",
            True
        ),
        pytest.param(
            "PASSWORD12@!",
            True
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
