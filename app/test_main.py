from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "test_case,expected_result",
    [
        pytest.param(
            "Pass1$@#&!-_",
            True,
            id="test should return true when all conditions"
        ),
        pytest.param(
            "qwerty",
            False,
            id="test should return false when no"
               " upper case and special symbol and number"
        ),
        pytest.param(
            "qwerty12",
            False,
            id="test should return false when no upper case an"
        ),
        pytest.param(
            "Qwertyui",
            False,
            id="test should return false when no number and special symbol"
        ),
        pytest.param(
            "Qwertyui1",
            False,
            id="test should return false when no special symbol"
        ),
        pytest.param(
            "Qwertyui#",
            False,
            id="test should return false when no digits"
        ),
        pytest.param(
            "Pass1$@#&!-_65426reyryyyi",
            False,
            id="test should return false when pass len > 16"
        ),
        pytest.param(
            "Pa1#",
            False,
            id="test should return false when pass len < 8"
        ),
        pytest.param(
            "рппр1115##",
            False,
            id="test should return false when not Latin Alphabet"
        )
    ]
)
def test_check_password(test_case: str, expected_result: bool) -> None:
    assert check_password(test_case) == expected_result
