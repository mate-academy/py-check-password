import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("mC1$apJ4knV0@yeRp", False),
        ("mC1$apJ4knV0@yeR", True),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("1P@sswd", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
