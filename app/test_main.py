import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password, expected",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Password1", False),
        ("password@1", False),
        ("PASSWORD@1", True),
        ("Pass@word", False),
        ("Pass word1@", False),
        ("Pass@word1!", True),
        ("P@1aaaaa", True),
        ("P@1" + "d" * 13, True),
        ("P@1" + "x" * 14, False),
        ("Paß@word1", False),
        ("12345678@", False),
        ("PASSWORD@", False),
        ("Pass@123", True),
    ],
    ids=[
        "valid basic",
        "no requirements",
        "too short",
        "no special",
        "no uppercase",
        "all upper valid",
        "no digit",
        "space not allowed",
        "multiple specials",
        "min length boundary",
        "max length boundary",
        "too long",
        "non latin letter",
        "no upper only digits special",
        "no digit only upper special",
        "valid simple",
    ]
)
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) is expected
