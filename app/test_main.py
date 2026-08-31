import pytest
from app.main import check_password


@pytest.mark.parametrize(
    "entered_password, result",
    [
        ("Pass@word1", True),
        ("Pass@word1abcdefg", False),
        ("Pass1abcdefgh", False),
        ("pass1@abcdefg", False),
        ("Pass@wordabcdefg", False),
        ("qwerty", False),
        ("A@c1", False),
        ("Str@ng", False)
    ]
)
def test_check_password(entered_password: str,
                        result: bool) -> None:
    assert check_password(entered_password) == result
