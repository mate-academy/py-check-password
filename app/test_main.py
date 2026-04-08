import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Str+ng39", False),
        ("password!2", False),
        ("uihv5K@", False),
        ("yehfbeuh!jHjxh1eil", False),
        ("Password@", False),
        ("Password1", False),

    ]
)

def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected
