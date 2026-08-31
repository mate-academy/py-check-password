import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        pytest.param(
            "radiohead2@", False,
            id="test upper requirement"
        ),
        pytest.param(
            "Thisc@ntainsrk123", False,
            id="test check max length"
        ),
        pytest.param(
            "Coolrobot17", False,
            id="check special character"
        ),
        pytest.param(
            "Hel17@", False,
            id="check minimum characters"
        ),
        pytest.param(
            "Vfwzkrfop@", False,
            id="test digit requirement"
        )
    ]
)
def test_password_requirements(
        password: str,
        expected: bool
) -> None:
    result = check_password(password)
    assert result == expected
