import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,validity",
    [
        pytest.param("", False, id="empty string is bnot valid"),
        pytest.param("Pass@word1", True, id="Pass@word1 is valid"),
        pytest.param("Pass @word1", False, id="space is not allowed"),
        pytest.param("Pass}word1", False, id="} is not allowed"),
        pytest.param(
            "Pass@word", False, id="password must contain at least 1 digit"
        ),
        pytest.param(
            "Password1",
            False,
            id="password must contain at least 1 special character",
        ),
        pytest.param(
            "pass@word1",
            False,
            id="password must contain at least uppercase letter",
        ),
        pytest.param(
            "PAssword197@",
            True,
            id="several special char, uppercase letters and digits is valid",
        ),
        pytest.param(
            "Pass@1", False, id="password's invalid if less 8 characters"
        ),
        pytest.param("Pass@word1Pass@wor", False, id="password is too long"),
    ],
)
def test_check_password(password: str, validity: bool) -> None:
    assert check_password(password) == validity
