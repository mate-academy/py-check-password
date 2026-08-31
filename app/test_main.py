import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="test when password is correct"
        ),
        pytest.param(
            "Pass@word1qwertyzxcv",
            False,
            id="test when password is too long"
        ),
        pytest.param(
            "Pa@1",
            False,
            id="test when password is too short"
        ),
        pytest.param(
            "1pass!word",
            False,
            id="test password without uppercase"
        ),
        pytest.param(
            "Password&",
            False,
            id="test when password without digits"
        ),
        pytest.param(
            "Password0",
            False,
            id="test password without special characters"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
