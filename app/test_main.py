import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "string_password, message_result",
    [
        pytest.param("Pass@word123456789", False, id="password too long"),
        pytest.param("Pas@1", False, id="too short password"),
        pytest.param("pass@word1", False, id="has not upper case"),
        pytest.param("Pass@word", False, id="without digits"),
        pytest.param("Password1", False, id="without special symbol"),
    ]
)
def test_check_password(
        string_password: str,
        message_result: bool
) -> None:
    assert check_password(string_password) == message_result
