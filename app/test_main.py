import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        ("Pass@word1", True),
        pytest.param(
            "Qwert1@",
            False,
            id="Password must be greater then 8 symbols"
        ),
        pytest.param(
            "Str@ngest",
            False,
            id="Password must contain numbers"
        ),
        pytest.param(
            "123456789Password@",
            False,
            id="Password must be less then 16 symbols"
        ),
        pytest.param(
            "Password123",
            False,
            id="Password must contain special character"
        ),
        pytest.param(
            "password@",
            False,
            id="Password must contain uppercase letter"
        ),
        pytest.param(
            "Password1+1",
            False,
            id="Password must contain symbols `$@#&!-`"
        ),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
