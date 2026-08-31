import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True, id="should be correct password"),
        pytest.param("qwertysss1-", False, id="should be no uper letter"),
        pytest.param("Qq1-", False, id="should be < 8"),
        pytest.param("123456789123456Ss-", False, id="should be > 16"),
        pytest.param("Pass@word1?", False, id="should be non symbols"),
        pytest.param("Pass@word", False, id="should be no digits"),
        pytest.param("Password1", False, id="should be no special symbols")
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
