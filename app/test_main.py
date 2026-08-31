import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="should return True if the pass is valid"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="should return False if the pass does not contain a digit"
        ),
        pytest.param(
            "Paaaaaaaaaaass@word1",
            False,
            id="should return False if the pass is too long"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="should return False if the pass doesnt contain upper-letter"
        ),
        pytest.param(
            "P@ss1",
            False,
            id="should return False if the pass is too short"
        ),
        pytest.param(
            "Password1",
            False,
            id="should return False if the pass does not contain a spec char"
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
