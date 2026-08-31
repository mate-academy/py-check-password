import pytest

from app import main


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="valid password"
        ),
        pytest.param(
            "Абвр68№1",
            False,
            id="all letters should be of the Latin alphabet"
        ),
        pytest.param(
            "Pass@w1Pass@w1Pass@w1",
            False,
            id="password's len should be maximum 16 characters inclusive"
        ),
        pytest.param(
            "Pass@w1",
            False,
            id="password's len should be at least 8 characters"
        ),
        pytest.param(
            "Pass@wgf",
            False,
            id="password should contain at least 1 digit"
        ),
        pytest.param(
            "pass@wgf1",
            False,
            id="password should contain at least 1 uppercase"
        ),
        pytest.param(
            "Wdsvgfcv1",
            False,
            id="password should contain at least 1 special symbol"
        )
    ]
)
def test_check_password_func(password: str, expected_result: bool) -> None:
    assert main.check_password(password) == expected_result
