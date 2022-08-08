import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected_result",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="correct password"
        ),
        pytest.param(
            "Qwe123!",
            False,
            id="password has less than 8 characters"
        ),
        pytest.param(
            "Qwerty@1234567890",
            False,
            id="password has more than 16 characters"
        ),
        pytest.param(
            "qwerty1!",
            False,
            id="password has no at least 1 uppercase letter"
        ),
        pytest.param(
            "Qwerty!!",
            False,
            id="password has no at least 1 digit"
        ),
        pytest.param(
            "Qwerty123",
            False,
            id="password has no at least 1 special character"
        ),
        pytest.param(
            "Qwerty123*",
            False,
            id="password has no accepted character"
        ),
    ]
)
def test_check_password(password, expected_result):
    assert check_password(password) == expected_result
