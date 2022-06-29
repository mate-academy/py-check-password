import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "actual_result, expected_result",
    [
        pytest.param(
            "Password123",
            False,
            id="should return False if password have not special symbols"
        ),
        pytest.param(
            "p@ssword123",
            False,
            id="should return False if password have not uppercase"
        ),
        pytest.param(
            "Password!!!",
            False,
            id="should return False if password have not digits"
        ),
        pytest.param(
            "P@ssword123",
            True,
            id="should return True if password have digits,"
               " uppercase, special symbols"
        ),
        pytest.param(
            "P@sw0",
            False,
            id="should return False if password length less 8"
        ),
        pytest.param(
            "P@ssw0rd1231231231",
            False,
            id="should return False if password length higher 17"
        )
    ]
)
def test_should_return_correct_values(actual_result, expected_result):
    assert check_password(actual_result) == expected_result
