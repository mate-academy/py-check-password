import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "q#erT4R", False,
            id="password less 8 characters should fail"
        ),
        pytest.param(
            "123$$hahahatooBIG!", False,
            id="password longer 16 characters should fail"
        ),
        pytest.param(
            "55alllower$", False,
            id="password without upper case should fail"
        ),
        pytest.param(
            "NoDigits@here", False,
            id="password without digits should fail"
        ),
        pytest.param(
            "noT2Spec1al", False,
            id="password without special symbols should fail"
        ),
    ]
)
def test_according_password_rules(password: str, expected: bool) -> None:
    assert check_password(password) == expected
