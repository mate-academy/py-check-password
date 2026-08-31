import pytest
from app.main import check_password


@pytest.mark.parametrize("user_password, expected", [
    ("Pass@word1", True),
    ("Pass@word1wwwwwww", False),
    ("Pass1@", False),
    ("Password@", False),
    ("Password12", False),
    ("password1@2", False)
])
def test_for_password(user_password: str, expected: bool) -> None:
    assert check_password(user_password) == expected
