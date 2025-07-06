import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, extended", [
        ("Pass#word1234", True),
        ("Pass#word1", True),
        ("Pass_word2", True),
        ("Pass-word3", True),
        ("Pass#word987654321", False),
        ("password5#", False),
        ("Pass word6", False),
        ("PASSWORD#", False),
        ("Password7", False),
        ("P#ssw8A", False),
        ("qwerty", False),
    ]
)
def test_check_password(password: str, extended: bool) -> None:
    assert check_password(password) is extended
