import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True,
                     id="test when password meet all 4 parameters"),
        pytest.param("Pass@word11234456e3473473473346346", False,
                     id="test when password is too long"),
        pytest.param("str@ng11", False,
                     id="test when password doesn't have upper case"),
        pytest.param("Qwert1@", False,
                     id="test when password is too short"),
        pytest.param("Pass@wordd", False,
                     id="test when password doesn't have digits"),
        pytest.param("Pass1wordd", False,
                     id="test when password doesn't have special symbols")

    ]
)
def test_returning_correct_value(password: str, result: bool) -> None:
    assert check_password(password) == result
