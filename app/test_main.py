import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="Pass@word1True",
        ),
        pytest.param(
            "qwerty",
            False,
            id="qwerty",
        ),
        pytest.param(
            "Str@ng",
            False,
            id="Str@ng",
        ),
        pytest.param(
            "qwertyqwe@rty1",
            False,
            id="qwertyqwe@rty1",
        ),
        pytest.param(
            "Password1",
            False,
            id="Password1",
        ),
        pytest.param(
            "A1@ss",
            False,
            id="A1@ss",
        ),
        pytest.param(
            "Pass@word1Pass@word1Pass@word1",
            False,
            id="Pass@word1Pass@word1Pass@word1",
        ),
        pytest.param(
            "Pas@sword",
            False,
            id="Pas@sword",
        ),

    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
