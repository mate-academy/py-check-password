import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_valid",
    [
        pytest.param(
            "Short", False,
            id="test password greater min length"
        ),
        pytest.param(
            "Too_loooong_passwoord", False,
            id="test password less than max length"
        ),
        pytest.param(
            "pass@word1", False,
            id="test password contains uppercase letters"
        ),
        pytest.param(
            "Pass@word1ю", False,
            id="test password contains only latin letters"
        ),
        pytest.param(
            "pass@word1", False,
            id="test password contains uppercase letters"
        ),
        pytest.param(
            "Pass@word", False,
            id="test password contains digits"
        ),
        pytest.param(
            "Passaword1", False,
            id="test password contains special symbols"
        ),
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
