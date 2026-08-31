import app.main as main

import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        pytest.param("Pass@word1", True),
        pytest.param("Qwer@1", False),
        pytest.param("Str@njslg", False),
        pytest.param("dhgtsy@d4is", False),
        pytest.param("klasdjflksadjflk@s1Udjflksdjklj", False),
        pytest.param("s1Udjflks3djklj", False),
    ],
)
def test_check_password(password: str, result: bool) -> None:
    assert main.check_password(password) == result
