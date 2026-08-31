import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Pass@word1", True,
            id="should return True when all requirements are met"
        ),
        pytest.param(
            "Pass@word", False,
            id="should return False when no digit"
        ),
        pytest.param(
            "Pass@word1Pass@word1", False,
            id="should return False when len > 16"
        ),
        pytest.param(
            "Pass@1", False,
            id="should return False when len < 8"
        ),
        pytest.param(
            "password@1", False,
            id="should return False when no uppercase"
        ),
        pytest.param(
            "Password1", False,
            id="should return False when no spec symbol"
        ),
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
