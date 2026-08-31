import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Pass@word", False),
        ("pass@word1", False),
        ("Password1", False),
        ("qwerty", False),
        ("Str@ng", False),
        ("dddddddddddM1@ddddddddddddd", False),
        ("mmM@mmmmmmmmmmm1", True),
        ("qW#rtyq1", True),
        ("qW#q1", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
