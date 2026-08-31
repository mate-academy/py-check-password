import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result", [
        pytest.param(
            "Pass@word1",
            True,
            id="should return true"
        ),
        pytest.param(
            "P@word1",
            False,
            id="should return false when pass less then 8 symbols"
        ),
        pytest.param(
            "P@w88888888ord1fds",
            False,
            id="should return false when pass more then 17 symbols"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="should return false when pass dont have digit"
        ),
        pytest.param(
            "Password1",
            False,
            id="should return false when pass dont have special symbols"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="should return false when pass dont have upper case"
        ),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert (
        check_password(password) == result
    )
