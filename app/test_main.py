import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="correct password"
        ),
        pytest.param(
            "q",
            False,
            id="should be at least 8 characters"
        ),
        pytest.param(
            "Pass@word1qwerty123",
            False,
            id="should be maximum 16 characters"
        ),
        pytest.param(
            "Pass@wordy",
            False,
            id="should contains at least 1 digit"
        ),
        pytest.param(
            "Password12",
            False,
            id="should contains at least 1 special character"
        ),
        pytest.param(
            "password@12",
            False,
            id="should contains at least 1 uppercase letter"
        ),
        pytest.param(
            "ІГОР-123",
            False,
            id="accepts only letters of the Latin alphabet Aa-Zz"
        ),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
