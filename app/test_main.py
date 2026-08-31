# write your code here
import pytest
from .main import check_password


@pytest.mark.parametrize(
    "password, result",
    [pytest.param("Pass@word1", True,
                  id="check that 'check_password' returns True"),
     pytest.param("qwerty", False,
                  id="check returns False for short passwords"),
     pytest.param("Pass@word", False,
                  id="check for passwords without digits"),
     pytest.param("Password1", False,
                  id="check for passwords without special character"),
     pytest.param("pass@word1", False,
                  id="check for passwords without uppercase letter"),
     pytest.param("Пass@word1", False,
                  id="check for passwords with different alfabet"),
     pytest.param("Pass@word111111111", False,
                  id="check for too long passwords")]
)
def test_check_password(password: str,
                        result: bool) -> None:
    assert check_password(password) == result
