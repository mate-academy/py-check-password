import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_string",
    [
        pytest.param(
            "Pass@word1ї",
            id="all letters should be within ASCII"
        ),
        pytest.param(
            "Pass@w1",
            id="length should be >= 8"
        ),
        pytest.param(
            "Pass@word1qqqqqqq",
            id="length should be <= 16"
        ),
        pytest.param(
            "Pass@word",
            id="must have at least 1 digit"
        ),
        pytest.param(
            "Password1",
            id="must have at least 1 special '$@#&!-_'"
        ),
        pytest.param(
            "pass@word1",
            id="must have at least 1 upper"
        ),
    ]
)
def test_wrong_pass(test_string: str) -> None:
    assert check_password(password=test_string) is False


def test_good_pass() -> None:
    assert check_password(password="Pass@word1") is True
