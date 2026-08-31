import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "P@word1",
            False,
            id="should return False if len lt 8"
        ),
        pytest.param(
            "Passdfghjfdghjk@word1",
            False,
            id="should return False if len mt 16"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="should return False if does not contains uppercase letter"
        ),

        pytest.param(
            "Password1",
            False,
            id="should return False if does not contains special character"
        ),

        pytest.param(
            "Pass@word",
            False,
            id="should return False if does not contains digit"
        )
    ]
)
def test_is_valid_password(password: str, result: bool) -> None:
    assert (
        check_password(password) is result
    )
