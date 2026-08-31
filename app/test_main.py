import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,goal",
    [
        pytest.param("1A@",
                     False,
                     id="password should have more than 8 symbols"
                     ),
        pytest.param("Itistoolongpassword123@",
                     False,
                     id="password should be not longer than 16"),
        pytest.param("noupper12@",
                     False,
                     id="password should accept upper letter"
                     ),

        pytest.param("UPPER12495",
                     False,
                     id="password should accept special character"),
        pytest.param("noNumber@",
                     False,
                     id="password should contain number"),
    ]
)
def test_password(password: str, goal: bool) -> None:
    assert check_password(password) == goal
