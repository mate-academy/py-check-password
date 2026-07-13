import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("Pass@wo1", True),
        ("Pass@wodddddddd1", True),
        ("Pass@wo", False),
        ("Pass@wodddddddd11", False),
        ("Password1", False),
        ("Pas@word", False),
        ("pass@word1", False),
        ("Pass@worд1", False),
        ("Pass%word1", False),
        ("Pass@ word1", False),
        ("", False),
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    result = check_password(password)
    assert result == expected
