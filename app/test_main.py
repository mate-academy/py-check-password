import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "pwd,result",
    [
        pytest.param("Str@ng1", False,
                     id="short passwords"),
        pytest.param("Pass@word13A!asd1", False,
                     id="too long passwords"),
        pytest.param("pass@word13", False,
                     id="passwords without uppercase letter"),
        pytest.param("Qwerty!A", False,
                     id="passwords without digits"),
        pytest.param("Password1", False,
                     id="passwords without special symbols"),
    ]
)
def test_func_check_password_with_param(pwd: str, result: bool) -> None:
    assert check_password(pwd) is result
