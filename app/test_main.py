import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("P@1a", False),
        ("VeryLongPassword123@", False),
        ("Password@", False),
        ("Password1", False),
        ("pass@word1", False),
        ("пароль*", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
