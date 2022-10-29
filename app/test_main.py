import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Pass@word1", True, id="is all right"),
        pytest.param("Pass@wordт", False, id="cyrillic symbol"),
        pytest.param("Pass@w1", False, id="less then 8 symbols"),
        pytest.param("Pass@word1Pass@word1", False, id="more then 16 symbols"),
        pytest.param("pass@word1", False, id="no uppercase"),
        pytest.param("Pass@word", False, id="no digits"),
        pytest.param("Password1", False, id="no special symbols")
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result
