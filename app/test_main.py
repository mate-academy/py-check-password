import pytest
from app import main


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("A1$aaaaa", True),
        ("A1$aaaaaaaaaaaaa", True),
        ("A1$aaaa", False),
        ("A@1", False),
        ("A1$aaaaaaaaaaaaaa", False),
        ("A1$aaaaaaaaaaaaaaa", False),
        ("pass@word1", False),
        ("a1$aaaaa", False),
        ("Pass@word", False),
        ("Aa$aaaaa", False),
        ("Password1", False),
        ("Aaaaaaaa1", False),
        ("Pass @ord1", False),
        ("Pass$word1", True),
        ("Pass@word1", True),
        ("Pass#word1", True),
        ("Pass&word1", True),
        ("Pass!word1", True),
        ("Pass-word1", True),
        ("Pass_word1", True),
        ("qwerty", False),
        ("", False),
    ],
)
def test_check_password(password: None, expected: None) -> None:
    assert main.check_password(password) is expected
