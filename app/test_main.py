import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("Pass@word1hgffdsrtyyu54@", False),
        ("Pa1ss@w", False),
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
