import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("", False),
        ("кирилиця", False),
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng1", False),
        ("Pass@word1Pass@word1Pass@word1", False),
        ("Password@", False),
        ("Password1", False),
        ("password@1", False),
    ]
)
def test_password(password: str, result: bool) -> None:
    assert check_password(password) == result
