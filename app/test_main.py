import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "P1@P1@P",
            False,
            id="Should return False if password < 8 symbols"
        ),
        pytest.param(
            "12345678901234P1@",
            False,
            id="Should return False if password > 16 symbols"
        ),
        pytest.param(
            "P1234567",
            False,
            id=(
                "Should return False if password does "
                "not contain the special character"
            )
        ),
        pytest.param(
            "P$@#&!-_",
            False,
            id="Should return False if password does not contain the digit"
        ),
        pytest.param(
            "1$@#&!-_",
            False,
            id=(
                "Should return False if password does "
                "not contain the uppercase letter"
            )
        ),
        pytest.param(
            "1$Qwerty;",
            False,
            id=(
                "Should return False if password contains "
                "the forbidden symbol"
            )
        ),
        pytest.param(
            "1$Qwerty",
            True,
            id="Should return False if password passes all checks"
        )
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
