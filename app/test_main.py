import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Pass@word1", True),
        ("qwerty11qqq@", False),
        ("1123qweqweQ", False),
        ("Sas@b1", False),
        ("qweqweqweqweQ1@qweqwe", False),
        ("qweqweQ@QQQ", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
