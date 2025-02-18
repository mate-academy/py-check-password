import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password , extend_result",
    [
        pytest.param(
            "Pass@word1", True,
            id="all requirements are met"
        ),
        pytest.param(
            "Pass@word1123456", True,
            id="upper number password check"
        ),
        pytest.param(
            "Pa1dg@qq", True,
            id="lower number password check"
        ),
        pytest.param(
            "Pas@1", False,
            id="crossing the lower limit"
        ),
        pytest.param(
            "Pass@word11234567qqqqqq", False,
            id="crossing the upper limit"
        ),
        pytest.param(
            "password", False,
            id="without upper letter, digit and special symbol"
        ),
        pytest.param(
            "password@8", False,
            id="without upper letter"
        ),
        pytest.param(
            "Password", False,
            id="without digit and special symbol"
        ),
        pytest.param(
            "P@ssword", False,
            id="without digit"
        ),
        pytest.param(
            "Password1", False,
            id="without special symbol"
        ),
        pytest.param(
            "1234567@", False,
            id="without letter"
        )
    ]
)
def test_valid_password(
        password: str,
        extend_result: bool
) -> None:
    assert check_password(password) == extend_result
