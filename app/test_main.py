import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "A$1", False, id="invalid, length < 8"
        ),
        pytest.param(
            "A$123456B@789101C", False, id="invalid, length > 16"
        ),
        pytest.param(
            "A$bCdeFghe", False, id="invalid, no digit"
        ),
        pytest.param(
            "A1bCd2Fghe", False, id="invalid, no special character"
        ),
        pytest.param(
            "1$23abcdefg", False, id="invalid, no uppercase letter"
        ),
        pytest.param(
            "A$1*34/56", False, id="invalid, has illegal characters"
        ),
        pytest.param(
            "A$123456", True, id="valid, length == 8"
        ),
        pytest.param(
            "A$1234561#abcdEF", True, id="valid, length == 16"
        ),
        pytest.param(
            "1G3@Bc456k75", True, id="valid, 8 <= length <= 16"
        )
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected, (
        f"unexpected result for '{password}'"
    )
