import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        ("A1@bcdef", True),
        ("A1@bcde", False),
        ("Abcdef1@ghijklm", True),
        ("Abcdef1@ghijklmn", True),
        ("Abcdef1@ghijklmnx", False),
        ("abcde1@gh", False),
        ("Abcde@gh", False),
        ("Abcde1gh", False),
        ("Valid1@Pass", True),
        ("Valid1@Pass$", True),
        ("Valid1@Pass%", False),
        ("A1@aaaaa", True),
        ("A1@aaaaaa", True),
        ("A1@aaaaaaa", True),
        ("A1@aaaaaaaa", True),
        ("A1@aaaaaaaaa", True),
        ("A1@aaaaaaaaaa", True),
        ("A1@aaaaaaaaaaa", True),
        ("A1@aaaaaaaaaaaa", True),
        ("A1@aaaaaaaaaaaaa", True),
        ("A1@aaaaaaaaaaaaaa", False),
        ("A1@aaaaaaaaaaaaaaa", False),
        ("A1$aaaaaa", True),
        ("A1@aaaaaa", True),
        ("A1#aaaaaa", True),
        ("A1&aaaaaa", True),
        ("A1!aaaaaa", True),
        ("A1-aaaaaa", True),
        ("A1_aaaaaa", True),
        ("A1;aaaaaa", True),
    ],
)
def test_check_password_boundaries(password: str, expected: bool) -> None:
    assert check_password(password) is expected
