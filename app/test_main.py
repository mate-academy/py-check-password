import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param("", False, id="empty string"),
        pytest.param("Qwy@1", False, id="short password"),
        pytest.param("QWERTY1E", False, id="password without special symbol"),
        pytest.param("qWErtyu@", False, id="password without digits"),
        pytest.param("qwerty1@", False, id="pass without uppercase letters"),
        pytest.param("Qwerty@1", True, id="good password"),
        pytest.param("qwerty1@Qwerty@1Qwty@1", False, id="too long password"),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
