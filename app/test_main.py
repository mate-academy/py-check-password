import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "pass@word1",
            False,
            id="test should check upper letter"
        ),
        pytest.param(
            "Pass@word12345678",
            False,
            id="test should check max length"
        ),
        pytest.param(
            "Pass@1",
            False,
            id="test should check min length"
        ),
        pytest.param(
            "Password123",
            False,
            id="test should check special symbols"
        ),
        pytest.param(
            "Pass@worddd",
            False,
            id="test should check digit"
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
