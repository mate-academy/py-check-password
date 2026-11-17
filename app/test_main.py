import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        pytest.param("qwerty", False, id="too short"),
        pytest.param("qwt!E12", False, id="too short"),
        pytest.param("password1@", False, id="no uppercase letter"),
        pytest.param(
            "Password1@",
            True,
            id="valid: upper+lower+digit+special"
        ),
        pytest.param("passwordQ!23sjaQ", True, id="valid: long with special"),
        pytest.param("password23sjaQF", False, id="no special char"),
        pytest.param(
            "passwordasdd",
            False,
            id="no digit, no upper, no special"
        ),
        pytest.param("passwordQ!23sjaQa", False, id="too long"),
        pytest.param("12345678", False, id="only digits"),
        pytest.param("stRong!@pas", False, id="no digit"),
    ]
)
def test_check_password(password: str, is_valid: bool) -> None:
    assert check_password(password) == is_valid
