import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, goal",
    [
        pytest.param("Pass@word", False,
                     id="False for passwords without digits"),
        pytest.param("Pass@1", False,
                     id="False for short passwords"),
        pytest.param("pass@word1", False,
                     id="False for passwords without uppercase letter"),
        pytest.param("Pass@word1Pass@word1", False,
                     id="False for too long passwords"),
        pytest.param("Password1", False,
                     id="False for passwords without special symbols"),
        pytest.param("Pass@word1", True,
                     id="Valid password"),
    ]
)
def test_check_password(password: str,
                        goal: bool) -> None:
    assert check_password(password) == goal
