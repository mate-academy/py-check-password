import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_output",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="valid password"
        ),
        pytest.param(
            "Short1@",
            False,
            id="Too short"
        ),
        pytest.param(
            "ThisIsTooLong1234!",
            False,
            id="too long"
        ),
        pytest.param(
            "pass@words1",
            False,
            id="without uppercase"
        ),
        pytest.param(
            "Pass@words",
            False,
            id="without digits"
        ),
        pytest.param(
            "Passwords1",
            False,
            id="without special character"
        )
    ]
)
def test_check_password(password: str, expected_output: bool) -> None:
    assert check_password(password) == expected_output
