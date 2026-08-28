from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Pass@12",
            False,
            id="check 7 chars",
        ),
        pytest.param(
            "Pass@123",
            True,
            id="check 8 chars",
        ),
        pytest.param(
            "Pass@123Pass@123",
            True,
            id="check 16 chars",
        ),
        pytest.param(
            "Pass@123Pass@1234",
            False,
            id="check 17 chars",
        ),
        pytest.param(
            "Pass@pass",
            False,
            id="missing digit",
        ),
        pytest.param(
            "Pass1234",
            False,
            id="missing special char",
        ),
        pytest.param(
            "pass@1234",
            False,
            id="missing uppercase char",
        ),
        pytest.param(
            "Pass@1$@#&!-_",
            True,
            id="all special chars",
        ),
        pytest.param(
            "Pass@1собака",
            False,
            id="not Latin chars",
        ),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
