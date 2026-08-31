import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password, is_valid",
    [
        ("", False),
        ("Aloha@4", False),
        ("Pass@word", False),
        ("Pass2word", False),
        ("pass2word", False),
        ("Pass@word1", True),
        ("Paфs@word1", False),
        ("Pass@word1Pass@wo", False),
    ]
)
def test_check_password(password: str, is_valid: bool)\
        -> None:
    assert check_password(password) == is_valid
