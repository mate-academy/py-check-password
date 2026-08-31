import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="valid password"
        ),
        pytest.param(
            "$qwerty2",
            False,
            id="not upper"
        ),
        pytest.param(
            "9991Asdf",
            False,
            id="not special symbol"
        ),
        pytest.param(
            "GeniusAA#",
            False,
            id="not digit"
        ),
        pytest.param(
            "R2&",
            False,
            id="short passwords"
        ),
        pytest.param(
            "!Ukraine24081991!",
            False,
            id="long passwords"
        )
    ]
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
