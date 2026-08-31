import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@word1", True,
            id="should be valid password"
        ),
        pytest.param(
            "qwerty", False,
            id="should be too short and lack digit or special"
        ),
        pytest.param(
            "Str@ng", False,
            id="should be too short"
        ),
        pytest.param(
            "12345678", False,
            id="should lack letters and special character"
        ),
        pytest.param(
            "password1", False,
            id="should lack uppercase and special character"
        ),
        pytest.param(
            "PASSWORD1", False,
            id="should lack special character"
        ),
        pytest.param(
            "Pass@word", False,
            id="should lack digit"
        ),
        pytest.param(
            "Pass@word1!", True,
            id="should be valid password with special character exclamation"
        ),
        pytest.param(
            "Valid1@Word", True,
            id="should be valid password with mixed characters"
        ),
        pytest.param(
            "123@_4567", False,
            id="should lack uppercase letter"
        ),
        pytest.param(
            "P@ssword123", True,
            id="should be valid password with special and digits"
        ),
        pytest.param(
            "A@1234567", True,
            id="should be valid short password"
        ),
        pytest.param(
            "TooLooooongPassword@1", False,
            id="should be too long"
        ),
        pytest.param(
            "Short1@", False,
            id="should be too short"
        ),
        pytest.param(
            "Pass@word1$#%", False,
            id="should contain invalid characters like '%'"
        ),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
