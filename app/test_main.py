import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param("Pas1@", False, id="return false if too short"),
        pytest.param(
            "Pas1@sword_very_long", False, id="return false if too long"
        ),
        pytest.param("Pas@sword", False, id="return false if not digits"),
        pytest.param(
            "Password1", False, id="return false if have no special symbols"
        ),
        pytest.param(
            "pas@sword1", False, id="return false if have no uppercase letter"
        ),
    ],
)
def test_return_correct_result(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
