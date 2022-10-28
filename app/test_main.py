import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "input_password,expected_result",
    [
        pytest.param(
            "Str@ngsdcs9329992",
            False,
            id="must be less than 16 characters",
        ),
        pytest.param(
            "St@r1",
            False,
            id="must be more than 8 characters",
        ),
        pytest.param(
            "_1strangers",
            False,
            id="passwords without uppercase letter",
        ),
        pytest.param(
            "Strangers",
            False,
            id="must be with special character and digits ",
        ),
        pytest.param(
            "#Strangers",
            False,
            id="must be for passwords with special character",
        ),
    ]
)
def test_correctly_input_password(input_password: str,
                                  expected_result: bool) -> None:
    assert check_password(input_password) == expected_result
