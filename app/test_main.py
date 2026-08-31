import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result_of_check",
    [
        pytest.param(
            "Pass@word1", True, id="password passes all checks"
        ),
        pytest.param(
            "7Fb!", False, id="less than 8 letters"
        ),
        pytest.param(
            "PASS!!!___4321wd@", False, id="more than 16 letters"
        ),
        pytest.param(
            "pass__23word", False, id="without upper letter"
        ),
        pytest.param(
            "Pass2353word", False, id="without special symbol"
        ),
        pytest.param(
            "Pass__@@@word", False, id="without numbers"
        ),
        pytest.param(
            "пароль$$&1234!", False, id="with non latin letters"
        ),
        pytest.param(
            {"password": 1234}, False, id="incorrect type"
        ),
    ]
)
def test_correct_check_password(
        password: str,
        result_of_check: bool
) -> None:
    assert check_password(password) == result_of_check
