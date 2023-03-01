import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "initial_password,expected",
    [
        pytest.param(
            "Pass@word", False,
            id="Check invalid password without digit"
        ), pytest.param(
            "Str@8", False,
            id="Check invalid too short password"
        ), pytest.param(
            "Str@nkjhdiuryjdh879987гнпffdlekfjg", False,
            id="Check invalid too long password"
        ), pytest.param(
            "633dqw@ttt", False,
            id="Check invalid password without uppercase letter"
        )
    ]
)
def test_check_password(initial_password: str, expected: bool) -> None:
    assert check_password(initial_password) == expected
