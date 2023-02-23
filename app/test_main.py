import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected_result",
    [
        ("abcdeF1$@#&!-_", True),
        ("A1#aaaa", False),
        ("Z9#zzzzz", True),
        ("A1#aaaaaaaaaaaaa", True),
        ("A1#aaaaaaaaaaaaaa", False),
        ("a1#aaaaa", False),
        ("A#aaaaaa", False),
        ("A1aaaaaa", False),
    ],
    ids=[
        "valid case",
        "at least size 8 chars",
        "size 8 chars",
        "size 16 chars",
        "maximum size 16 chars",
        "must contains at least 1 uppercase",
        "must contains at least 1 digit",
        "must contains at least 1 special char"
    ]
)
def test_check_password(
        password: str,
        expected_result: bool
) -> None:
    assert check_password(password) == expected_result
