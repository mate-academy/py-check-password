import pytest
from app import main


@pytest.mark.parametrize(
    "input_pass,result",
    [
        ("", False),
        ("Pass@word1", True),
        ("qwerty", False),
        ("qw@rty15", False),
        ("Str@ng", False),
        ("PASS@WORD1", True),
        ("Ps@wor2", False),
        ("Woooooooooooord@12", False),
        ("Pytest_numb!", False),
        ("AdekWhat1", False)
    ]
)
def test_check_password(
        input_pass: str,
        result: bool
) -> None:
    assert main.check_password(input_pass) == result
