from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "qwerty",
            False,
        ),
        pytest.param(
            "Str@ng",
            False,
        ),
        pytest.param(
            "Fab&23",
            False,
        ),
        pytest.param(
            "dsj@dffs!fsf",
            False,
        ),
        pytest.param(
            "Act1hvvv@jskaHkafjdf#",
            False,
        ),
        pytest.param(
            "Abcdef1@",
            True,
            id="valid: minimal case"
        ),
        pytest.param(
            "Zorro123#",
            True, id="valid: upper, digit, special"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
