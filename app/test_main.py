import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="should return True when password is valid"
        ),
        pytest.param(
            "Password1",
            False,
            id="should return False when no special symbols are in password"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="should return False when no digits are in password"
        ),
        pytest.param(
            "password",
            False,
            id="should return False when no uppercase letters are in password"
        ),
        pytest.param(
            "Word@1",
            False,
            id="should return False when password is too short"
        ),
        pytest.param(
            "Password_password_password@1",
            False,
            id="should return False when password is too long"
        ),
        pytest.param(
            "Password@1Ш",
            False,
            id="should return False when unacceptable symbol in password"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
