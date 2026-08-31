import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "Qwert1@",
            False,
            id="should be at least 7 characters long"
        ),
        pytest.param(
            "Qwerty1@asdfarhra",
            False,
            id="should be less than 17 characters long"
        ),
        pytest.param(
            "Qwert1@trafф",
            False,
            id="should not contain non-latin symbols"
        ),
        pytest.param(
            "qwert1@traf",
            False,
            id="should contain at least 1 uppercase letter"
        ),
        pytest.param(
            "Qwert@traf",
            False,
            id="should contain at least 1 digit"
        ),
        pytest.param(
            "Qwert1traf",
            False,
            id="should contain at least one special symbol"
        ),
        pytest.param(
            "Qwert1@traf",
            True,
            id="should accept correct passwords"
        )
    ]
)
def test_should_assess_passwords_correctly(
        password: str,
        expected: bool
) -> None:
    assert check_password(password) is expected
