import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,is_pass",
    [
        ("Pass@word1", True),
        ("Pass@wo1", True),
        ("Pass@word1$#&!-_", True),
        ("Pass@word1%", False),
        ("Pass@11", False),
        ("Pass@word1$#&!-_@", False),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False)
    ],
    ids=[
        "Valid",
        "8 characters",
        "16 characters",
        "Have invali spatial character",
        "Too small - 7 characters",
        "Too big - 17 characters",
        "No digit",
        "No special character",
        "No uppercase letter"
    ]
)
def test_check_password(password: str, is_pass: bool) -> None:
    assert check_password(password) is is_pass
