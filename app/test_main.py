import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("", False),
        ("Q1@pas", False),
        ("Qwerty1234567890@", False),
        ("Q2@password111word", False),
        ("qwertyuiop@1", False),
        ("Qwerty1231", False),
        ("Qwerty@@@@", False),
        ("Password1%", False),
        ("QWERTY#123", True),
        ("Pass@word1", True)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
