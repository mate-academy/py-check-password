import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "pass",
            False,
            id="should be at least 8 characters",
        ),
        pytest.param(
            "secret@123_password",
            False,
            id="should be at most 16 characters",
        ),
        pytest.param(
            "Pass@word1",
            True,
            id="should be valid",
        ),
        pytest.param(
            "Pass@word",
            False,
            id="should contain at least one digit",
        ),
        pytest.param(
            "pass@word1",
            False,
            id="should contain at least one upper letter",
        ),
        pytest.param(
            "Password1",
            False,
            id="should contain at least one of `$@#&!-_`",
        ),
        pytest.param(
            "Pass@word1Й",
            False,
            id="should accepts only Latins, digits or special symbols",
        ),
    ],
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
