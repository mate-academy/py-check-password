import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        pytest.param(
            "1@Qwert",
            False,
            id="Password is shorter than 8 symbols"
        ),
        pytest.param(
            "1Qwertya",
            False,
            id="Password must contain at least one special symbol($@#&!-_)"
        ),
        pytest.param(
            "@Qwertya",
            False,
            id="Password must contain at least one digit(0-9)"
        ),
        pytest.param(
            "1@qwerty",
            False,
            id="Password must contain at least one upper symbol"
        ),
        pytest.param(
            "1@Qwerty",
            True,
            id="1@Qwerty is valid password"
        ),
        pytest.param(
            "Qwerty1@Qwerty1@1",
            False,
            id="Password longer than 16 symbols"
        )
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
