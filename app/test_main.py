import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param(
            "Fa1$",
            False,
            id="Should have at least 8 symbols"
        ),
        pytest.param(
            "Passworabcdefghijklmnopar123@",
            False,
            id="Should have no more than 16 symbols"
        ),
        pytest.param(
            "Password@@@",
            False,
            id="Should have at least one digit"
        ),
        pytest.param(
            "Password123",
            False,
            id="Should have at least one special character"
        ),
        pytest.param(
            "passwordpassword123@",
            False,
            id="Should have at least one uppercase letter"
        ),
        pytest.param(
            "Password123@$!",
            True,
            id="Should return 'True' if password is valid"
        )
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
