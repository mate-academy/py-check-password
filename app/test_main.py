import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param("", False, id="no password"),
        pytest.param("Pass@word1", True, id="good password"),
        pytest.param("xF1!", False, id="too short password"),
        pytest.param("Pass@word1asdasdasd", False, id="too long password"),
        pytest.param("password!1", False, id="password has no upper"),
        pytest.param("passworD1", False, id="password has no spec sumbol"),
        pytest.param("passwoR!", False, id="password has no digit"),
        pytest.param("xftofososd", False, id="only low letter"),
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
