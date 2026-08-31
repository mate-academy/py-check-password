import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_password",
    [
        pytest.param(
            "-Test12", False,
            id="Should return error pass too short"
        ),
        pytest.param(
            "@Password1234567890", False,
            id="Should return error pass too long"
        ),
        pytest.param(
            "#test123", False,
            id="should return error without uppercase letter"
        ),
        pytest.param(
            "!!!!Test", False,
            id="Should return error without digits"
        ),
        pytest.param(
            "Test1234", False,
            id="Should return error without special symbols"
        ),
    ]
)
def test_check_password(password, expected_password):
    assert check_password(password) == expected_password
