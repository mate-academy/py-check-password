import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param("Aqwer12!*", False, id="unsupported special character"),
        pytest.param("Qhjrty9&", True, id="8 symbols"),
        pytest.param("Asdfghjkl9876$_-", True, id="16 symbols"),
        pytest.param("As876$_", False, id="7 symbols"),
        pytest.param("Asdfghjkl90876$_-", False, id="17 symbols"),
        pytest.param("Lkjhhgf$_", False, id="no digit"),
        pytest.param("kkks876$_", False, id="no uppercase"),
        pytest.param("As876jsla", False, id="no special character"),

    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
