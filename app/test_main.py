import pytest
from .main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("S1tr@ngdcvwvvgsegwegcsadcsac", False),
        ("123456df", False),
        ("A2@e", False),
        ("A2@48er", False),
        ("q@1rtyfg", False),
        ("Ra1rtyfg", False),
        ("Ra@rtyfg", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    password_check = check_password(password)
    assert password_check == result
