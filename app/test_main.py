import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_bool",
    [
        pytest.param(
            "Pass@678",
            True,
            id="test correct password with min characters"
        ),
        pytest.param(
            "Pass@678Pass@456",
            True,
            id="test correct password with max characters"
        ),
        pytest.param(
            "A@с4567",
            False,
            id="test password less than 8 characters"
        ),
        pytest.param(
            "A@345678911234567",
            False,
            id="test password bigger than 16 characters"
        ),
        pytest.param(
            "Qwerty@adf",
            False,
            id="test password without digits"
        ),
        pytest.param(
            "1234Qwerty",
            False,
            id="test password without special character"
        ),
        pytest.param(
            "1234@qwerty",
            False,
            id="test password without uppercase letter"
        ),
    ]
)
def test_should_return_expected_error(password, expected_bool):
    assert check_password(password) == expected_bool
