import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Non@ngPassw@rd12345", False),
        ("Bad@огр123", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
