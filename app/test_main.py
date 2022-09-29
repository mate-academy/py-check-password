from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        pytest.param(
            "12345",
            False,
            id="pass contains only digits"
        ),
        pytest.param(
            "Str12345",
            False,
            id="pass has no special char"
        ),
        pytest.param(
            "Str@1",
            False,
            id="pass is too short"
        ),
        pytest.param(
            "Qwerty12312341241245@12",
            False,
            id="pass is too long"
        ),
        pytest.param(
            "Ass@rted1",
            True,
            id="OK"
        ),
        pytest.param(
            "IWould@like",
            False,
            id="pass has no digits"
        ),
        pytest.param(
            "123_qwerty",
            False,
            id="pass with no special symbols"
        )
    ]
)
def test_check_password(password, result):
    assert check_password(password) == result
