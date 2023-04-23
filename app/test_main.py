import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "word, result",
    [
        ("Pass@word1", True),  # all correct,
        ("password@123", False),  # no uppercase letters
        ("Password123", False),  # no special symbols
        ("Password@#$", False),  # no digits
        ("12345#$%&*", False),  # no letters
        ("Pass@12", False),  # len 7
        ("Pass@123", True),  # len 8
        ("Password@1234567", True),  # len 16
        ("Password@12345678", False)  # len 17
    ]
)
def test_check_password(word: str, result: bool) -> None:
    assert check_password(word) == result
