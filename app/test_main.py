import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,correct_output",
    [
        pytest.param(
            "Pass@word123456789101112",
            False,
            id="too long"
        ),
        pytest.param(
            "Pass@word",
            False,
            id="no digits"
        ),
        pytest.param(
            "pass@word12",
            False,
            id="no uppercase"
        ),
        pytest.param(
            "Pass@w1",
            False,
            id="too short"
        ),
        pytest.param(
            "Password12",
            False,
            id="no special symbol"
        ),
    ]
)
def test_func(password: str, correct_output: bool) -> None:
    assert check_password(password) == correct_output
