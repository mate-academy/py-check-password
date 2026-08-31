import pytest

from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("Password@", False),
    ("Password1", False),
    ("password@1", False),
    ("Pass@1", False),
    ("Pass@word1Pass@word1", False),
    ("Pass@word1!", True),
    ("A1@bcdef", True),
    ("A1@bcdefghijklmn", True),
    ("A1@bcde", False),
    ("A1@bcdefghijklmno", False),
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
