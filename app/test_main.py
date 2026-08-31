import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, check_result",
    [
        ("Pass@word1", True),
        ("A1@bcde", False),
        ("Password1", False),
        ("Pass%word1", False),
        ("AAAAAAAA1@", True),
        ("aaaaaaaa1@", False),
        ("Password@", False),
        ("Abcdefghij1@KLmno", False),
    ],
)
def test_check_password(password: str, check_result: bool) -> None:
    assert check_password(password) == check_result
