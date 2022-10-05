from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "m1a@tE",
            False,
            id="password is too short"
        ),
        pytest.param(
            "Str@ngest",
            False,
            id="password has no digits"
        ),
        pytest.param(
            "pass@word1",
            False,
            id="password has no upper letters"
        ),
        pytest.param(
            "TOOOOOOL00ONGP@SSWORD",
            False,
            id="password is too long"
        ),
        pytest.param(
            "passWORD12",
            False,
            id="password has no special symbol"
        ),
        pytest.param(
            "Pass@word1",
            True,
            id="correct password"
        )
    ]
)
def test_check_password(password, result):
    assert check_password(password) is result
