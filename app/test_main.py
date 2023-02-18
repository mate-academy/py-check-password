import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("qwerty", False),
        ("Str@ng", False),
        ("Pass@word1fushfshsduf", False),
        ("P@1", False),
        ("Pass@word", False),
        ("pass@word1", False)
    ]
)
def test_check_password(password: str, result: bool) -> None:
    assert check_password(password) == result
