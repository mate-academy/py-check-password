import pytest
from app.main import check_password


@pytest.mark.parametrize("password, expected", [
    ("Pass@word1", True),
    ("qwerty", False),
    ("sH0$", False),
    ("aass@word1", False),
    ("PASSWORD", False),
    ("Str@ng", False),
    ("AbC12345@", True),
    ("$pecialP@ss", False),
    ("1234$AbCdEfG56789,", False),
    ("NoSpecial123", False),
    ("OnlyUpperCase", False),
    ("12345678", False),
    ("ToLong12345&passWord", False),
    ("", False)
])
def test_check_password(password: str, expected: bool) -> None:
    assert check_password(password) == expected


if __name__ == "__main__":
    pytest.main()
