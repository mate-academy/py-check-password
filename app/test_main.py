import pytest


from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@wordd",
            False,
            id="checking for the presence of digits"
        ),
        pytest.param(
            "Pa@rd1",
            False,
            id="check for short password"
        ),
        pytest.param(
            "Pa@rd1dfsdfdsfsdfsdfdsfsdfd",
            False,
            id="check for a long password"
        ),
        pytest.param(
            "pass@wordd1",
            False,
            id="uppercase check"
        ),
        pytest.param(
            "Password1",
            False,
            id="check for special characters"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
