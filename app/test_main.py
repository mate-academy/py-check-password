from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "initial_password, expected_decision",

    [
        pytest.param(
            "Pass",
            False
        ),
        pytest.param(
            "Pass@word1adadsadsadswdadwawaawdadw",
            False
        ),
        pytest.param(
            "Pass@word1",
            True
        ),
        pytest.param(
            "Pass@wordde",
            False
        ),
        pytest.param(
            "Password123",
            False
        ),
        pytest.param(
            "pass@word1",
            False
        ),
        pytest.param(
            "Pas@1",
            False
        ),
    ]
)
def test_main(initial_password: str, expected_decision: bool) -> None:
    assert check_password(initial_password) == expected_decision
