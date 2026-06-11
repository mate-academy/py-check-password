import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Pass@word1", True),
        ("My@word2", True),
        ("Mytruepass@word2", True),
        ("qwe1@S", False),
        ("Hello2026world!@@", False),
        ("Str@nger", False),
        ("Str0nger", False),
        ("str0nger@", False),
        ("", False),
    ]
)
def test_check_password(word: str, expected: bool) -> None:
    assert check_password(word) == expected
