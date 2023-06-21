import pytest

from .main import check_password


@pytest.mark.parametrize(
    "password, respond",
    [
        ("Pass@word1", True),
        ("Pass@word1Pass@word1", False),
        ("pass@word1", False),
        ("Pass@word", False),
        ("Password1", False),
        ("P@a1", False),
    ]
)
def test_password(password: str, respond: bool) -> None:
    assert check_password(password) == respond
