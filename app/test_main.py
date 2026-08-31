from app.main import check_password

import pytest


@pytest.mark.parametrize(
    "password,expected_result",
    [
        pytest.param(
            "@fdJfdA38!_Vb-$#",
            True,
            id="test password length = 16"),
        pytest.param(
            "#3nG1bGV",
            True,
            id="test password length = 8"),
        pytest.param(
            "$gCEUfw03gs6km!#9",
            False,
            id="password length should be <= 16"
        ),
        pytest.param(
            "#UoyD84",
            False,
            id="password length should be > 8"),
        pytest.param(
            ".lsAf()fd){}",
            False,
            id="password should not contain unsupported chars",
        ),
        pytest.param(
            "kAfr@Jh&Oj",
            False,
            id="password should contain at least 1 digit"
        ),
        pytest.param(
            "uOLleK111m",
            False,
            id="password should contain at least 1 special character",
        ),
        pytest.param(
            "j2ox8ab$yk",
            False,
            id="password should contain at least 1 uppercase letter",
        ),
    ],
)
def test_check_password(password: str, expected_result: bool) -> None:
    assert check_password(password) == expected_result
