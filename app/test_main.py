import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_output",
    [
        ("miNlen8!", True),
        ("PassmaxLength16!", True),
        ("NotSupSymb@@./_", False),
        ("123456789", False),
        ("NoDigits!", False),
        ("TomanySymbolsOutofRange!1234", False),
        ("nouppercase01!", False),
        ("1!Pp", False)
    ]
)
def test_check_password(
        password: str,
        expected_output: bool
) -> None:
    assert check_password(password) == expected_output
