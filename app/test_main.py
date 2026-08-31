from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password, result",
    [
        ("Pass@word1", True),
        ("Pass@word1Pass@word1Pass@word1", False),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("P@d1", False),
    ]
)
def test(password: str, result: bool) -> None:
    assert check_password(password) == result
