import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("Pass@word1", True, id="Correct password"),
        pytest.param("qwerty", False, id="Lower case + short"),
        pytest.param("Str@ng", False, id="Too short password"),
        pytest.param("Password", False, id="Without special characters"),
        pytest.param("PasswordPassword1", False, id="Too long password"),
        pytest.param("Pass@word1Pass@w", True, id="16 char password"),
        pytest.param("Passwоrd@1", False, id="Non Latin char"),
        pytest.param("P@sswor1", True, id="8 char password"),
    ]
)
def test_valid_password(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) == expected
