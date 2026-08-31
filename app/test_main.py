import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param(
            "Pass@world1", True
        ),
        pytest.param(
            "qwerty", False
        ),
        pytest.param(
            "Str@ng", False
        ),
        pytest.param(
            "Rva7je#", False
        ),
        pytest.param(
            "rwe&ikEa5rtt87r35", False
        ),
    ]
)
def test_should_return_valid_password(
        password, expected_result
):
    assert check_password(password) == expected_result
