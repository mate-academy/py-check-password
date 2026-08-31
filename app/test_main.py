import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Longyyy@012345678", False),
        ("Short1@", False),
        ("Str@nggg", False),
        ("qwerty@7", False),
        ("Qwerty01", False),
    ],
    ids=[
        "correct combination",
        "exceeded max length",
        "lack of min length",
        "omit digit",
        "omit upper",
        "omit special"
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
