import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "Pass@word1", True,
            id="Strong password 'Pass@word1'"
        ),
        pytest.param(
            "Password", False,
            id="Password should contain at least 1 special character"
        ),
        pytest.param(
            "q@3", False,
            id="Password should contain at least 8 characters"
        ),
        pytest.param(
            "Pass@w00000000000000000000000rd", False,
            id="Password should not be large that 16 symbols"
        ),
        pytest.param(
            "Крутий@Пароль228", False,
            id="Password should contain only Latin chars"
        )
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
