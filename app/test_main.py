import app.main as main

import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True, id="Valid password"),
        pytest.param("WithOutDig#", False, id="Add digital"),
        pytest.param("WithOutSpec1", False, id="Add special"),
        pytest.param("Small#1", False, id="Short password"),
        pytest.param("TooLo0o0o0o0o0o0ongPass#1", False, id="Long"),
        pytest.param("lowercase#1", False, id="Add uppercase"),
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert main.check_password(password) == result
