import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True,
                     id="Test correct password"),
        pytest.param("qwerty", False,
                     id="Test qwerty password"),
        pytest.param("Str@ng", False,
                     id="Test short password length when other rules correct"),
        pytest.param("Pass@word1Str@ng123", False,
                     id="Test long password length when other rules correct"),
        pytest.param("П@роль123", False,
                     id="Test if text in Cyrillic"),
        pytest.param("P@@s$@#&!1", True,
                     id="Test if many special characters"),
    ]
)
def test_check_password(
        password: str,
        result: bool
) -> None:
    assert check_password(password) == result
