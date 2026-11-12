import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="Is valid password"
        ),
        pytest.param(
            "qwerty",
            False,
            id="No digit, no special character, no upper case and too short"
        ),
        pytest.param(
            "abcdefghijklmnopqrstuvwxyz",
            False,
            id="No digit, no special character, no upper case and too long"
        ),
        pytest.param(
            "unbelievable",
            False,
            id="No digit, no special character, no upper case"
        ),
        pytest.param(
            "Password1",
            False,
            id="No special character"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="No upper case"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="No digit"
        ),
        pytest.param(
            "Pass@word1234567890",
            False,
            id="Too long password > 16 characters"
        ),
        pytest.param(
            "Pas@1d",
            False,
            id="Too short password < 8 characters"
        ),
        pytest.param(
            "Str@ng",
            False,
            id="No digit and too short password < 8 characters"
        ),
        pytest.param(
            "Str@ngest1234567890",
            False,
            id="No digit and too long password > 16 characters"
        ),
        pytest.param(
            "Strong1",
            False,
            id="No special character and too short password < 8 characters"
        ),
        pytest.param(
            "Strongest1234567890",
            False,
            id="No special character and too long password > 16 characters"
        ),
        pytest.param(
            "str@ng1",
            False,
            id="No uppercase and too short password < 8 characters"
        ),
        pytest.param(
            "str@ngest1234567890",
            False,
            id="No uppercase and too long password > 16 characters"
        ),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
