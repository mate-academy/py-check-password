from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param("Pass@word1", True, id="valid pass"),
        pytest.param("Pass@word", False, id="without digits"),
        pytest.param("Pass@1", False, id="short pass"),
        pytest.param("pass@word1", False, id="without uppercase"),
        pytest.param("Pass@word1Pass@word1", False, id="too long"),
        pytest.param("Password1", False, id="without symbols")
    ]
)
def test_check_password_correctly(password: str, expected: bool) -> None:
    assert check_password(password) == expected
