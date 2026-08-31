import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "aA1$bcd",
            False,
            id="should return False if length < 8",
        ),
        pytest.param(
            "aA1$bcdefghijklmn",
            False,
            id="should return False if length > 16",
        ),
        pytest.param(
            "aa1$bcde",
            False,
            id="should return False if there are no uppercase letters",
        ),
        pytest.param(
            "aAa$bcdefghijklm",
            False,
            id="should return False if there are no digits",
        ),
        pytest.param(
            "aA10bcde",
            False,
            id="should return False if there are no special characters",
        ),
        pytest.param(
            "aA1$bcde",
            True,
            id="should return True for `aA1$bcde`",
        ),
    ],
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) is expected_result
