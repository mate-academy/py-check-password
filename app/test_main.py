import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "test_password, result",
    [
        ("Kjjj4@f", False),
        ("Pass@word12345678", False),
        ("Pass@word1", True),
        ("Pass@word1234567", True),
        ("Pas@word", False),
        ("Password1", False),
        ("pass@word1", False)
    ]
)
def test_check_password(test_password: str, result: bool) -> None:
    assert check_password(test_password) == result
