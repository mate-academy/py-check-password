import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_password, result", [
        pytest.param(
            "Pass@word1ksdkeiie",
            False,
            id="should return False if password is too long"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="should return False if password has no digits"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="should return False if password has no uppercase letter"
        ),
        pytest.param(
            "Pass@w1",
            False,
            id="should return False if password is too short"
        ),
        pytest.param(
            "Password1",
            False,
            id="should return False if password has no special symbols"
        )
    ]
)
def test_check_password(test_password: str, result: bool) -> None:
    password = test_password
    assert check_password(password) == result
