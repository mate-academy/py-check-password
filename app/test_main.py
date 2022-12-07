import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "actual,excepted",
    [
        pytest.param(
            "qwerty1234@",
            False,
            id="password should has 1 uppercase letter"
        ),
        pytest.param(
            "Qwerty1234",
            False,
            id="password should has 1 special character"
        ),
        pytest.param(
            "Qwerty@qwe",
            False,
            id="password should has 1 digit"
        ),
        pytest.param(
            "Pass@word11111111",
            False,
            id="password should have maximum 16 characters inclusive"
        ),
        pytest.param(
            "Pass@w1",
            False,
            id="password should have least 8 characters"
        )
    ]
)
def test_without_upper_letter(
        actual: str,
        excepted: bool) -> None:
    assert check_password(actual) == excepted
